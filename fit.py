import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'fitness_pot'
app.config["MONGO_URI"] = 'mongodb+srv://tomciosegal:cucharec7164@myfirstcluster-nbawd.mongodb.net/fitness_pot?retryWrites=true&w=majority'

mongo = PyMongo(app)
import pymongo
import pprint

myclient = pymongo.MongoClient("mongodb+srv://tomciosegal:cucharec7164@myfirstcluster-nbawd.mongodb.net")
mydb = myclient["fitness_pot"]
mycol = mydb["dish"]

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

def home_page1():
     pprint.pprint(mycol.find_one({"category": "dinner"}))
     return mycol.find_one()

@app.route('/myrecipies')
def myrecipies():
    return render_template('myrecipies.html')



if __name__ == '__main__':
    app.run(host=os.environ.get('IP','0.0.0.0'),
            port=int(os.environ.get('PORT','8080')),
            debug=True)