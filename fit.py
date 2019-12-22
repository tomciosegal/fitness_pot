import os
from flask import Flask, render_template, redirect, request, url_for, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 
import json
from flask_login import LoginManager
from flask_login import current_user, login_user
from dotenv import load_dotenv

load_dotenv()
print(os.environ)
app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'fitness_pot'
app.config["MONGO_URI"] = 'mongodb+srv://tomciosegal:cucharec7164@myfirstcluster-nbawd.mongodb.net/fitness_pot?retryWrites=true&w=majority'
login = LoginManager(app)
mongo = PyMongo(app)


import pymongo
import pprint

myclient = pymongo.MongoClient("mongodb+srv://tomciosegal:cucharec7164@myfirstcluster-nbawd.mongodb.net")
mydb = myclient["fitness_pot"]
mycol = mydb["dish"]
userscol = mydb["users"]
x = mydb.list_collection_names()


@app.route('/')
def index():
    pagination = 6
    next = True
    recipes = mydb.dish.find()
    try:
        page=int(request.args.get("page",1))
    except ValueError:
        page = 1
    if page < 1:
        page = 1
    start = int(pagination * (page -1))
    stop = int(pagination * page)
    recipes = [x for x in recipes]
    if stop > len(recipes):
        next = False
    recipes = recipes[start:stop] 
    return render_template("index.html",page=page,recipes=recipes, next=next)




@app.route('/breakfast')
def breakfast():
    return render_template('breakfast.html')

@app.route('/dinner')
def dinner():
    return render_template('dinner.html')

@app.route('/dessert')
def dessert():
    return render_template('dessert.html')

@app.route('/drinks')
def drinks():
    return render_template('drinks.html')

@app.route('/vegan')
def vegan():
    return render_template('vegan.html')

# @app.route('/allrecipies')
# def allrecipies():
#     recipies = mydb.dish.find()
#     return render_template('allrecipies.html', recipies=recipies)

        

def home_page1():
     pprint.pprint(mycol.find_one({"category": "dinner"}))
     return mycol.find_one()

@app.route('/addrecipie')
def addrecipie():
    return render_template('addrecipie.html')

@app.route('/myrecipies')
def myrecipies():
    mydb.dish.find({"user_id": user_id})
    return render_template('myrecipies.html')

@app.route('/recipe_details')
def recipe_details():
    action = request.args.get('action')
    recipe = request.args.get('recipe')

    the_recipe = mongo.db.dish.find_one({"_id": ObjectId(recipe)})
    
    if action == 'index':
        return render_template("recipe_details.html", recipe=the_recipe)
    elif action == 'edit':
        return render_template("edit_recipe.html", recipe=the_recipe)
    elif action == 'delete':
        mongo.db.recipes.delete_one({"_id": ObjectId(recipe)})
        return render_template("recipes.html", recipes=mongo.db.recipes.find())

@app.route('/create_user', methods = ['POST'])
def createuser():
    newuser = {
        "username": request.form.get('username'),
        "password": request.form.get('password'),
        "email": request.form.get('email')
    }
    userscol.insert_one(newuser)
    return 'SUCCESS'
    
@app.route('/login', methods = ['POST'])
def login():
    username =  request.form.get('username')
    password = request.form.get('password')
    userfromdb = userscol.find_one({ "username": username })
    if (userfromdb != None and userfromdb['password'] == password):
        # login_user(userfromdb)
        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

   

@app.route('/createrecepie', methods = ['POST'])
def createrecepie():
    print (request.form.get('user_name'))
    newrecipe = {"title" :"test recepie", 
              "category" : "vegan",
              "image" : "test_image.jpeg",
              "cooking_time" : "40",
              "serves" : "2",
              "calories" : "100",
              "author" : "John",
              "ingredients" : "a,b,c",
              "instructions" : "dsfdgfdsf",
              "nutrition" : "fbfgdsdf"
        }
    mycol.insert_one(newrecipe)
    return 'TEST'



if __name__ == '__main__':
    app.run(host=os.environ.get('IP','0.0.0.0'),
            port=int(os.environ.get('PORT','8080')),
            debug=True)