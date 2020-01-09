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
from flask_pymongo import PyMongo
from utilities import paginate
from validators import validate_recipe

load_dotenv()

app = Flask(__name__)
app.config["MONGO_DBNAME"] = "fitness_pot"
app.config["MONGO_URI"] = os.environ["MONGO_URI"]
app.config["SECRET_KEY"] = "qwert"
login = LoginManager(app)
mongo = PyMongo(app)


myclient = pymongo.MongoClient(os.environ.get("MONGO_CLUSTER"))
mydb = myclient["fitness_pot"]
mycol = mydb["dish"]
userscol = mydb["users"]
x = mydb.list_collection_names()


DEBUG_LEVEL = "DEBUG"


@app.route("/", methods=["GET", "POST"])
def index():
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
    categories = set(
        [x.get("category") for x in mydb.dish.find() if x.get("category")]
    )

    return render_template(
        "index.html",
        page=page,
        recipes=recipes,
        next=next,
        categories=categories,
        selected_category=selected_category,
        should_show_background_image=True,
    )


@app.route("/login", methods=["POST", "GET"])
def login():
    users = mongo.db.users
    login_user = users.find_one({"username": request.form["username"]})
    if login_user:
        if request.form["password"] == login_user["password"]:
            session["username"] = request.form["username"]
            session["logged_in"] = True
            flash("Welcome " + session["username"], "success")
            return redirect(url_for("index"))
    return redirect(url_for("index"))


@app.route("/logout", methods=["GET"])
def logout():
    if session.get("logged_in"):
        session["logged_in"] = False
        session.pop("username")
        flash("You are logged out!")
        return redirect(url_for("index"))
    else:
        return render_template("index.html")


def home_page1():
    pprint.pprint(mycol.find_one({"category": "dinner"}))
    return mycol.find_one()


@app.route("/addrecipe")
def addrecipe():
    categories = set(
        [x.get("category") for x in mydb.dish.find() if x.get("category")]
    )
    return render_template(
        "addrecipe.html",
        recipe=None,
        text="Add Recipe",
        button_text="Add new recipe",
        form_action="createrecepie",
        categories=categories,
        should_show_background_image=False,
    )


@app.route("/myrecipies")
def myrecipies():
    return render_template("myrecipies.html")


@app.route("/recipe_details")
def recipe_details():
    action = request.args.get("action")
    recipe = request.args.get("recipe")
    categories = set(
        [x.get("category") for x in mydb.dish.find() if x.get("category")]
    )

    the_recipe = mongo.db.dish.find_one({"_id": ObjectId(recipe)})
    print("the_recipe : ", the_recipe)
    if action == "index":
        return render_template(
            "recipe_details.html",
            recipe=the_recipe,
            should_show_background_image=False,
        )
    elif action == "edit":
        print("the_recipe", the_recipe)
        the_recipe["parsed_ingredients"] = parse_array(
            the_recipe.get("ingredients")
        )
        return render_template(
            "addrecipe.html",
            recipe=the_recipe,
            text="Edit Recipe",
            categories=categories,
            button_text="Update recipe",
            form_action="updaterecepie",
            should_show_background_image=False,
        )
    elif action == "delete":
        mycol.delete_one({"_id": ObjectId(recipe)})
        return redirect(url_for("index"))


@app.route("/create_user", methods=["POST"])
def createuser():
    newuser = {
        "username": request.form.get("username"),
        "password": request.form.get("password"),
        "email": request.form.get("email"),
    }
    userscol.insert_one(newuser)
    return "SUCCESS"


@app.route("/createrecepie", methods=["POST"])
def createrecepie():
    print("request.form.get(ingredients) = ", request.form.get("ingredients"))
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

    if DEBUG_LEVEL == "DEBUG":
        print("newrecipe = ", newrecipe)
    print(request.form.to_dict())
    if is_valid:
        mycol.insert_one(newrecipe)
        return redirect(url_for("index"))
    categories = set(
        [x.get("category") for x in mydb.dish.find() if x.get("category")]
    )
    return render_template(
        "addrecipe.html",
        recipe=None,
        text="Add Recipe",
        button_text="Add new recipe",
        form_action="createrecepie",
        categories=categories,
        should_show_background_image=False,
        message="All fields are mandatory",
    )


@app.route("/updaterecepie", methods=["POST"])
def updaterecepie():
    print("i am in updaterecepie")
    recipe_id = request.form.get("recipe_id")
    print(request.form)
    print("id", recipe_id)

    newrecipe = {
        "$set": {
            "name": request.form.get("name"),
            "user_name": session.get("username"),
            "title": request.form.get("title"),
            "serves": request.form.get("serves"),
            "mail": request.form.get("mail"),
            "image": request.form.get("image_url"),
            "ingredients": request.form.get("ingredients"),
            "instructions": request.form.get("instructions"),
        }
    }

    mycol.update_one({"_id": ObjectId(recipe_id)}, newrecipe)
    

    return redirect(url_for("index"))


def parse_array(input_array):
    out = ""
    for v in input_array:
        out = out + v + "\n"

    return out


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "8080")),
        debug=True,
    )
