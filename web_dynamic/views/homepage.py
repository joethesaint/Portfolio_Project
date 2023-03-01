from flask import jsonify, render_template, redirect, request
import json
from models import storage
from models.city import City
from models.food import Food
from models.restaurant import Restaurant
from web_dynamic.views import app_views

@app_views.route("/")
def index():
    foods = storage.all(Food)
    restaurant = storage.all(Restaurant)
    return render_template("index.html", top_restaurants=restaurant, top_foods=foods, new_restaurants=restaurant, new_foods=foods)


@app_views.route("/search", methods=['POST', 'GET'])
def search():
    cities = storage.all(City)
    restaurants = storage.all(Restaurant)
    if request.method == "POST":
        data_list = []
        data = json.loads(request.data)
        if data['resource'] == "food":
            foods = storage.all(Food)
            if data['location'] == "none":
                for food in foods:
                    data_list.append(food.to_dict())

                return jsonify({
                'fetched': True,
                'data': data_list,
                'resource_type': 'food',
                'heading': 'All Meals'
                })
            else:
                location = storage.get(City, data['location'])
                if location:
                    for rest in restaurants:
                        if rest.city_id == location.id:
                            for food in rest.foods:
                                data_list.append(food.to_dict())
                    return jsonify({
                        'fetched': True,
                        'data': data_list,
                        'resource_type': 'food',
                        'heading': 'All Meals in {}'.format(location.name)
                    })

        if data['resource'] == "restaurant":
            if data['location'] == "none":
                for rest in restaurants:
                    data_list.append(rest.to_dict())
                return jsonify({
                'fetched': True,
                'data': data_list,
                'resource_type': 'restaurant',
                'heading': 'All Restaurants'
                })

            else:
                location = storage.get(City, data['location'])
                if location:
                    for rest in restaurants:
                        if rest.city_id == location.id:
                            data_list.append(rest.to_dict())
                    return jsonify({
                        'fetched': True,
                        'data': data_list,
                        'resource_type': 'restaurant',
                        'heading': 'Restaurants in {}'.format(location.name)
                        })

        return jsonify({
            'fetched': True,
            'data': data_list,
            'resource_type': 'none',
            'heading': 'All {} in {}'.format(data['resource'], location.name)
        })
    return render_template('search.html', cities=cities, restaurants=restaurants)


