import os
import requests
from flask import Flask, request, redirect, render_template, url_for
from flask_pymongo import PyMongo
import json
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()
# Define API KEY, ENDPOINTS, AND HEADERS HERE
API_KEY = os.getenv('API_KEY')
API_URL = 'https://api.yelp.com/v3'
BUSINESS_ENDPOINT = 'https://api.yelp.com/v3/businesses/search'
HEADERS = {'Authorization': 'bearer %s' % API_KEY}
# Define our parameters
PARAMETERS = {
    'categories': 'food',
    'limit': 20,
    'radius': 10000,
    'price': 1,
    'is_close': False,
    'location': 'Oakland'
}
# Make a request to the API
response = requests.get(url=BUSINESS_ENDPOINT,
                        params=PARAMETERS, headers=HEADERS)

business_name = []
rating = []
price = []
address = []
photo = []

# Converts the json string to a dictionary
category_data = response.json()

for biz in category_data['businesses']:
    business_name.append(biz['name']),
    rating.append(biz['rating']),
    price.append(biz['price']),
    address.append(biz['location']),
    photo.append(biz['image_url'])

print(business_name)
print(rating)


@ app.route('/')
def displayWelcomePage():
    return render_template('index.html')


@ app.route('/home')
def display_categories():
    business = {
        'business_name': business_name,
        'rating': rating,
        'price': price,
        'address': address,
        'photo': photo,
        'limit': 20
    }

    context = {
        'business_data': business
    }
    return render_template('home.html', **context, business=business)


@ app.route('/about')
def meetUs():
    return render_template('about.html')


@ app.route('/feed')
def feedPage():
    return render_template('feed.html')


@ app.route('/post')
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
    display_categories()
