from flask import Flask, request, redirect, render_template, url_for
import json
import os
from dotenv import load_dotenv
import requests
# from flask_pymongo import PyMongo
# from bson.objectid import ObjectId
app = Flask(__name__)

# app.config['MONGO_URI'] = "mongodb+srv://merissa:Tigers98!@cluster0.emrvw.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
# mongo = PyMongo(app)


@app.route('/')
def displayWelcomePage():
    return render_template('index.html')


@app.route('/home')
def displayHomePage():
    return render_template('home.html')


@app.route('/about')
def meetUs():
    return render_template('about.html')


@app.route('/feed')
def feedPage():
    return render_template('feed.html')


@app.route('/post')
def postPage():
    return render_template('post.html')




@app.route('/listings')
def listing():
    try:
        return render_template('listing.html')
    except (ValueError, TypeError):
        return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=True)
