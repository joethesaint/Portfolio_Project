from flask import render_template, session, redirect, request, session, flash
from hashlib import md5
import json
from models import storage
from models.user import User
from web_dynamic.views import app_views


@app_views.route('validate_email', methods=['POST'])
def validate_email():
    if request.method == "POST":
        print(request.url)
        email_dict = json.loads(request.data.decode('utf-8'))
        print(email_dict)
        for user in storage.all(User):
            if user.email == email_dict['email']:
                return {"valid": False}
    return {"valid": True}


@app_views.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        request.form['email']
        request.form['password']
        password = md5(bytes(request.form['password'], 'UTF-8')).hexdigest()
        print(password, type(password))
        users = storage.all(User)
        for user in users:
            if request.form['email'] == user.email and password == user.password:
                session['logged_in'] = True
                session['user_id'] = user.id
        if session.get('logged_in', None) is None:
            flash('Incorrect email or password!', category='danger')
        else:
            return redirect('/')
    return render_template("login.html")


@app_views.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        fname = request.form['first-name']
        lname = request.form['last-name']
        email = request.form['email']
        password = request.form['password']
        field = dict(request.form)

        if len(fname) < 1 or len(lname) < 1 or len(email) < 1 or len(password) < 7:
            return render_template('register.html', field=field)
        new_user = User(first_name=fname, last_name=lname, email=email, password=password)
        new_user.save()
        flash('Registration successful. Log in', category='success')
        return redirect('login')

    return render_template('register.html')


@app_views.route('/logout')
def logout():
    if 'user_id' in session.keys() or 'logged_in' in session.keys():
        del session['user_id']
        del session['logged_in']
    return redirect('/')
