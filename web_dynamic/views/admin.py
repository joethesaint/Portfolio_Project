#!/usr/bin/python3

from flask import flash, session, request, render_template
from models import storage
from models.city import City
from models.food import Food
from models.restaurant import Restaurant
from models.user import User
from web_dynamic.views import app_views

@app_views.route('/add_restaurant', methods=['GET', 'POST'])
def add_restaurant():
    if session.get('user_id', None) is None:
        flash('You must be logged in to do this', category='info')
        return render_template('admin/add_restaurant.html')

    if storage.get(User, session.get('user_id', None)).email[:5] != "admin":
        flash('You are not authorised to do this', category='danger')
        return render_template('admin/add_restaurant.html')

    cities = storage.all(City)
    if request.method == "POST":
        if len(request.form['name']) < 3:
            flash('Restaurant name is to short', category='danger')
            return render_template('admin/add_restaurant.html', cities=cities, field=request.form)
        if len(request.form['address']) < 5:
            flash('Address should be detailed', category='danger')
            return render_template('admin/add_restaurant.html', cities=cities, field=request.form)
        if len(request.form['description']) < 100:
            flash('The dexcription is too short', category='danger')
            return render_template('admin/add_restaurant.html', cities=cities, field=request.form)
        if storage.get(City, request.form['city']) is None:
            flash('Invalid locaction/city', category='danger')
            return render_template('admin/add_restaurant.html', cities=cities, field=request.form)

        r = Restaurant(name=request.form['name'], address=request.form['address'], description=request.form['description'], city_id=request.form['city'])
        r.save()

        flash('Restaurant Added', category='success')

    return render_template('admin/add_restaurant.html', cities=cities)


@app_views.route('/add_food', methods=['GET', 'POST'])
def add_food():
    if session.get('user_id', None) is None:
        flash('You must be logged in to do this', category='info')
        return render_template('admin/add_food.html')

    if storage.get(User, session.get('user_id', None)).email[:5] != "admin":
        flash('You are not authorised to do this', category='danger')
        return render_template('admin/add_food.html')

    restaurants = storage.all(Restaurant)
    restaurants = sorted(restaurants, key=lambda k: k.name)
    if request.method == "POST":
        restaurant = storage.get(Restaurant, request.form['restaurant'])
        if restaurant is None:
            flash('Invalid restaurant', category='danger')
            return render_template('admin/add_food.html', restaurants=restaurants, field=request.form)
        if len(request.form['name']) < 2:
            flash('Food name is to short', category='danger')
            return render_template('admin/add_food.html', restaurants=restaurants, field=request.form)
        if float(request.form['price']) < 2.00:
            flash('Food too cheap', category='danger')
            return render_template('admin/add_food.html', restaurants=restaurants, field=request.form)
        if len(request.form['description']) < 100:
            flash('The dexcription is too short', category='danger')
            return render_template('admin/add_food.html', restaurants=restaurants, field=request.form)

        f = Food(name=request.form['name'], price=request.form['price'], description=request.form['description'], restaurant_id=request.form['restaurant'])
        f.save()

        flash('Meal Added to {}'.format(restaurant.name), category='success')

    return render_template('admin/add_food.html', restaurants=restaurants)

