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
# def hello():
#     return 'Hello World ...again'
def index():
    # pprint.pprint(mycol.find_one({"title": "Spicy Thai Sweet Potato Soup"}))
    return render_template("index.html")


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

@app.route('/allrecipies')
def allrecipies():
    recipies = mydb.dish.find()
    return render_template('allrecipies.html', recipies=recipies)

        

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
    data = []
    with open("data/recipe.json", "r") as json_data:
        data = json.load(json_data)
    # recipies = mydb.dish.find_one()
    return render_template('recipe_details.html', recipe_details=data)

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