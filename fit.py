import os
import pprint

import pymongo
from bson.objectid import ObjectId
from dotenv import load_dotenv
from flask import (
    Flask,
    flash,
    redirect,
    render_template,
    request,
    session,
    url_for,
)
from flask_login import LoginManager
from utilities import paginate
from validators import validate_recipe

load_dotenv()

app = Flask(__name__)
# Get secret key
app.config["SECRET_KEY"] = "qwert"
login = LoginManager(app)

# Mongo Database for FITNESS POT
myclient = pymongo.MongoClient(os.environ.get("MONGO_CLUSTER"))
mydb = myclient["fitness_pot"]
dish_col = mydb["dish"]
users_col = mydb["users"]
collection_names = mydb.list_collection_names()


DEBUG_LEVEL = "DEBUG"

# =========
# HOME PAGE - Display home page featured recipes with image and introductory text only
# =========


@app.route("/", methods=["GET", "POST"])
def index():
    # this will allow to display 6 recipes per page. function located in utilities.py file
    pagination = 6
    recipes = mydb.dish.find()

    selected_category = "All Recipes"

    if request.args.get("category"):
        selected_category = (
            request.args.get("category").capitalize() + " Recipes"
        )

    if request.args.get("category"):
        recipes = mydb.dish.find({"category": request.args.get("category")})

    recipes, page, next = paginate(
        recipes, pagination, request.args.get("page")
    )
    return render_template(
        "index.html",
        page=page,
        recipes=recipes,
        next=next,
        categories=get_all_categories_from_db(),
        selected_category=selected_category,
        should_show_background_image=True,
    )


# =================================
# LOGIN MODAL- function will allow create new account
# ==================================
@app.route("/create_user", methods=["POST"])
def createuser():
    newuser = {
        "username": request.form.get("username"),
        "password": request.form.get("password"),
        "email": request.form.get("email"),
    }

    try:
        ret = users_col.insert_one(newuser)
        flash(
            "Congratulation "
            + request.form.get("username")
            + "! You have created account"
        )
    # try and except to notify user in case there was some troubleshooting
    except:
        flash(
            "Sorry, there was some problem, user "
            + request.form.get("username")
            + " was not added to database"
        )
        print(e)

    return redirect(url_for("index"))


# =================================
# LOGIN MODAL- function will allow login to created account
# ==================================
@app.route("/login", methods=["POST", "GET"])
def login():
    login_user = mydb.users.find_one({"username": request.form["username"]})
    if login_user:
        if request.form["password"] == login_user["password"]:
            session["username"] = request.form["username"]
            session["logged_in"] = True
            flash("Welcome " + session["username"])
            return redirect(url_for("index"))


# =================================
# LOGOUT MODAL- function will allow logout from account
# ==================================
@app.route("/logout", methods=["GET"])
def logout():
    if session.get("logged_in"):
        session["logged_in"] = False
        session.pop("username")
        flash("You are logged out!")
        return redirect(url_for("index"))
    else:
        return render_template("index.html")


# =============================
# DISPLAY 'MY RECIPES' SCREEN - Allowing user in input a or view, edit, delete only users recipes
# =============================
@app.route("/myrecipies")
def myrecipies():
    pagination = 6

    user = session.get("username")
    if user:
        recipes = mydb.dish.find({"user_name": user})
    else:
        recipes = []

    recipes, page, next = paginate(
        recipes, pagination, request.args.get("page")
    )

    return render_template(
        "myrecipies.html", page=page, recipes=recipes, next=next,
    )


@app.route("/recipe/delete/<recipe_id>", methods=["GET", "POST"])
def delete_recipe(recipe_id):
    try:
        dish_col.delete_one({"_id": ObjectId(recipe_id)})
        flash("You have deleted recipe")
    except:
        flash("Deleting not succesfull")

    return redirect(url_for("index"))


@app.route("/recipe/edit/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if request.method == "POST":
        updated_recipe = {
            "$set": {
                "category": request.form.get("category"),
                "title": request.form.get("title"),
                "serves": request.form.get("serves"),
                "image": request.form.get("image_url"),
                "name": request.form.get("name"),
                "ingredients": list(
                    request.form.get("ingredients").split("\n")
                ),
                "instructions": list(
                    request.form.get("instructions").split("\n")
                ),
                "user_name": session.get("username"),
            }
        }
        try:
            dish_col.update_one({"_id": ObjectId(recipe_id)}, updated_recipe)
            flash("Your recipe was updated")
        except:
            flash("Recipe not updated,try again")

        return redirect(url_for("view_recipe", recipe_id=recipe_id))
    elif request.method == "GET":
        the_recipe = mydb.dish.find_one({"_id": ObjectId(recipe_id)})

        the_recipe["parsed_ingredients"] = ""
        for ing in the_recipe["ingredients"]:
            the_recipe["parsed_ingredients"] = (
                the_recipe["parsed_ingredients"] + ing
            )

        the_recipe["parsed_instructions"] = ""
        for ins in the_recipe["instructions"]:
            the_recipe["parsed_instructions"] = (
                the_recipe["parsed_instructions"] + ins
            )

        return render_template(
            "edit_recipe.html",
            recipe=the_recipe,
            text="Edit Recipe",
            categories=get_all_categories_from_db(),
            button_text="Update recipe",
            form_action="updaterecepie",
            should_show_background_image=False,
        )


@app.route("/recipe/view/<recipe_id>")
def view_recipe(recipe_id):
    recipe = mydb.dish.find_one({"_id": ObjectId(recipe_id)})
    return render_template(
        "recipe_details.html",
        recipe=recipe,
        should_show_background_image=False,
    )


@app.route("/recipe/new", methods=["GET", "POST"])
def create_recipe():
    if request.method == "POST":
        # actions for POST
        # here are adding recipe to DB
        (request.form.to_dict())
        is_valid = validate_recipe(request.form)
        newrecipe = {
            "category": request.form.get("category"),
            "title": request.form.get("title"),
            "serves": request.form.get("serves"),
            "image": request.form.get("image_url"),
            "ingredients": list(request.form.get("ingredients").split("\n")),
            "instructions": list(request.form.get("instructions").split("\n")),
            "user_name": session.get("username"),
        }

        if is_valid:
            try:
                dish_col.insert_one(newrecipe)
                flash("Dish was added")
            except:
                flash("Dish was not added")
        else:
            flash("Input values are wrong")

        return redirect(url_for("index"))
    elif request.method == "GET":
        # actions for GET
        # here we show form in HTML
        return render_template(
            "addrecipe.html",
            categories=get_all_categories_from_db(),
            should_show_background_image=False,
        )

    # return render_template(
    #     "addrecipe.html",
    #     recipe=None,
    #     text="Add Recipe",
    #     button_text="Add new recipe",
    #     form_action="createrecepie",
    #     categories=get_all_categories_from_db(),
    #     should_show_background_image=False,
    #     message="All fields are mandatory",
    # )


# @app.route("/updaterecepie/<recipe_id>", methods=["POST"])
# def updaterecepie(recipe_id):
#     newrecipe = {
#         "$set": {
#             "name": request.form.get("name"),
#             "user_name": session.get("username"),
#             "title": request.form.get("title"),
#             "serves": request.form.get("serves"),
#             "mail": request.form.get("mail"),
#             "image": request.form.get("image_url"),
#             "ingredients": request.form.get("ingredients"),
#             "instructions": request.form.get("instructions"),
#         }
#     }

#     dish_col.update_one({"_id": ObjectId(recipe_id)}, newrecipe)

#     return redirect(url_for("index"))


# def parse_array(input_array):
#     out = ""
#     for v in input_array:
#         out = out + v + "\n"
#     return out


def get_all_categories_from_db():
    categories = set(
        [
            collection_names.get("category")
            for collection_names in mydb.dish.find()
            if collection_names.get("category")
        ]
    )
    return categories


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "8080")),
        debug=True,
    )
