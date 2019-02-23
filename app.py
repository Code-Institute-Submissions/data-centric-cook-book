import os
from flask import Flask, render_template ,redirect, request, url_for, flash,session
from flask_pymongo import PyMongo, pymongo


app = Flask(__name__)
app.secret_key = 'Ernesto_papa'
app.config["MONGO_DBNAME"] = "cook_book"
app.config["MONGO_URI"] = "mongodb://admin:dimension123@ds125574.mlab.com:25574/cook_book"

mongo = PyMongo(app)

@app.route('/')
@app.route("/home", methods=['POST','GET'])
def home():
    recipes = mongo.db.recipes.find()
    return render_template('index.html',recipes=recipes)

# this route displays recipes in the database
@app.route('/add_recipe')
def add_recipe():
    return render_template('add_recipe.html', 
    categories = mongo.db.categories.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
        
        