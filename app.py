import os
import requests
from flask import Flask, request, redirect, render_template, url_for
from flask_pymongo import PyMongo
import json
# from bson.objectid import ObjectId
from dotenv import load_dotenv
app = Flask(__name__)

app.config['MONGO_URI'] = "mongodb+srv://merissa:Tigers98!@cluster0.emrvw.mongodb.net/Web1-1?retryWrites=true&w=majority"
mongo = PyMongo(app)

load_dotenv()
# Define API KEY, ENDPOINTS, AND HEADERS HERE
API_KEY = os.getenv('API_KEY')
API_URL = 'https://api.yelp.com/v3'
CATEGORY_ENDPOINT = 'https://api.yelp.com/v3/categories/food'
BUSINESS_ENDPOINT = 'https://api.yelp.com/v3/businesses/search'

HEADERS = {'Authorization': 'bearer %s' % API_KEY}

# Define our parameters
PARAMETERS = {
    'categories': 'food',
    'limit': 20,
    'radius': 10000,
    'price': 1,
    'is_close': False,
    #   'location': location
}

# Make a request to the API

response = requests.get(url=BUSINESS_ENDPOINT,
                        params=PARAMETERS, headers=HEADERS)


# print(json.dumps(category_data, indent=3))

# for item in category_data['businesses']:
#     print(item['name'], item['rating'],
#           item['price'], item['location']['address1'], item['is_closed'], item['image_url'])


@ app.route('/')
def displayWelcomePage():
    return render_template('index.html')


@ app.route('/home')
def display_categories():

    # Converts the json string to a dictionary
    category_data = requests.get(url=BUSINESS_ENDPOINT,
                                 params=PARAMETERS, headers=HEADERS).json()

    business_name = []
    rating = []
    price = []
    address = []
    photo = []

    json.dumps(category_data, indent=3)

    for item in category_data['businesses']:
        business_name.append(item['name'])
        rating.append(item['rating'])
        price.append(item['price'])
        address.append(item['display_address'])
        photo.append(item['image_url'])

    context = {
        'business_name': business_name,
        'rating': rating,
        'price': price,
        'address': address,
        'photo': photo,
        'limit': 20
    }
    return render_template('home.html', **context)


@ app.route('/about')
def meetUs():
    return render_template('about.html')


@ app.route('/feed')
def feedPage():
    return render_template('feed.html')


@ app.route('/post')
def postPage():
    return render_template('post.html')


if __name__ == '__main__':
    app.run(debug=True)
