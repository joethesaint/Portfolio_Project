#!/usr/bin/python3
"""Starts a Flask Web App"""
from models import storage
from flask import Flask, render_template
from flask_session import Session
from web_dynamic.views import app_views


app = Flask(__name__)
app.config['SESSION_COOKIE_SECURE'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = 900
app.config['SESSION_USE_SIGNER'] = True
app.config['SESSION_TYPE'] = 'filesystem'
app.secret_key = "My Secret Key"
app.url_map.strict_slashes = False
Session(app)
app.register_blueprint(app_views, url_prefix="/")

@app.teardown_appcontext
def close_db(error):
    """Remove the current SQLAlchemy Session"""
    storage.close()

@app.errorhandler(404)
def not_found(err):
    """404 Error response"""
    return render_template("404.html"), 404

@app.errorhandler(500)
def not_found(err):
    """500 Error response"""
    return render_template("500.html"), 500

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
