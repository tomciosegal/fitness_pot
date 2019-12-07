import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'fitness_pot'
app.config["MONGO_URI"] = 'mongodb+srv://tomciosegal:cucharec7164@myfirstcluster-nbawd.mongodb.net/fitness_pot?retryWrites=true&w=majority'

mongo = PyMongo(app)
@app.route('/')
def hello():
    return 'Hello World ...again'


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)