from flask import jsonify, render_template, request
import json
from models import storage
from models.city import City
from models.food import Food
from models.restaurant import Restaurant
from web_dynamic.views import app_views

@app_views.route("/")
def index():
    foods = storage.all(Food)
    restaurants = storage.all(Restaurant)
    top_restaurants = sorted(restaurants, key=lambda k: (k.get_rating()['len'], k.get_rating()['total']), reverse=True)[:8]
    # top_restaurants = sorted(top_restaurants, key=lambda k: k.get_rating()['total'], reverse=True)

    top_foods = sorted(foods, key=lambda k: (k.get_rating()['len'], k.get_rating()['total']), reverse=True)[:8]

    new_restaurants = sorted(restaurants, key=lambda k: k.created_at, reverse=True)[:8]

    new_foods = sorted(foods, key=lambda k: k.created_at, reverse=True)[:8]
    return render_template("index.html", top_restaurants=top_restaurants, top_foods=top_foods, new_restaurants=new_restaurants, new_foods=new_foods)


@app_views.route("/search", methods=['POST', 'GET'])
def search():
    cities = storage.all(City)
    restaurants = storage.all(Restaurant)
    cities = sorted(cities, key=lambda k: k.name)
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


