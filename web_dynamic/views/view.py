from models import storage
from models.city import City
from models.food import Food
from models.food_review import FoodReview
from models.restaurant import Restaurant
from models.restaurant_review import RestaurantReview
from models.user import User
from web_dynamic.views import app_views
from flask import flash, render_template, request, redirect, abort, session


@app_views.route("/restaurants/<id>")
def get_restaurant(id):
    """Gets a restaurants and displays info about it"""
    restaurant = storage.get(Restaurant, id)
    city = storage.get(City, restaurant.city_id)

    if not restaurant:
        abort(404)

    return render_template("restaurant.html", restaurant=restaurant, city=city)


@app_views.route("/foods/<id>")
def get_food(id):
    """Gets a food and displays info about it"""
    food = storage.get(Food, id)
    restaurant = storage.get(Restaurant, food.restaurant_id)
    if restaurant:
        print(restaurant.name)

    if not food:
        abort(404)

    return render_template("food.html", restaurant=restaurant, food=food)


@app_views.route("/restaurants/reviews")
def view_restaurant_review():
    restaurant = storage.all(Restaurant)[0]
    restaurant_review = restaurant.reviews[0]
    user = storage.get(User, restaurant_review.user_id)
    return render_template("restaurant_review.html", review=restaurant_review, restaurant=restaurant, user=user)


@app_views.route('/restaurants/review/<id>', methods=['GET', 'POST'])
def review_restaurant(id):
    print(id)
    url = request.url
    restaurant_id = url.split('/')[-1]
    restaurant = storage.get(Restaurant, restaurant_id)

    if not restaurant:
        abort(404)
    
    if request.method == 'POST':
        if session.get('user_id', None) is None:
            flash('Please login to submit review', category='info')
            return redirect(request.url)
        
        user = storage.get(User, session['user_id'])
        reviews = storage.all(RestaurantReview)
        for review in reviews:
            if review.user_id == session['user_id'] and review.restaurant_id == restaurant_id:
                flash('Already reviewed this Restaurant', category='info')
                return redirect(request.url)
        ambience = int(request.form['ambience'])
        cleanliness = int(request.form['clean'])
        service = int(request.form['service'])
        uniqueness = int(request.form['unique'])
        description = request.form['description']

        r_r = RestaurantReview(ambience=ambience, cleanliness=cleanliness, service=service, uniqueness=uniqueness, text=description, restaurant_id=restaurant.id, user_id=session['user_id'])
        r_r.save()
        return redirect('/restaurants/{}'.format(restaurant_id))
    
    return render_template('review.html', restaurant=restaurant)


@app_views.route("/foods/reviews")
def view_food_review():
    food = storage.all(Food)[0]
    food_review = food.reviews[0]
    user = storage.get(User, food_review.user_id)
    return render_template("food_review.html", review=food_review, food=food, user=user)


@app_views.route('/foods/review/<id>', methods=['GET', 'POST'])
def review_food(id):
    print(id)
    url = request.url
    food_id = url.split('/')[-1]
    food = storage.get(Food, food_id)

    if not food:
        abort(404)
    
    if request.method == 'POST':
        if session.get('user_id', None) is None:
            flash('Please login to submit review', category='info')
            return redirect(request.url)
        
        user = storage.get(User, session['user_id'])
        reviews = storage.all(FoodReview)
        for review in reviews:
            if review.user_id == session['user_id'] and review.food_id == food_id:
                flash('Already reviewed this Food', category='info')
                return redirect(request.url)
        appearance = int(request.form['appear'])
        execution = int(request.form['exec'])
        quality = int(request.form['quality'])
        taste = int(request.form['taste'])
        description = request.form['description']

        r_r = FoodReview(appearance=appearance, execution=execution, quality=quality, taste=taste, text=description, food_id=food.id, user_id=session['user_id'])
        r_r.save()
        return redirect('/foods/{}'.format(food_id))
    
    return render_template('review_food.html', food=food)
