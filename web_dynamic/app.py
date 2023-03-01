#!/usr/bin/python3
"""Starts a Flask Web App"""
from models import storage
from flask import Flask, jsonify, make_response, render_template
from web_dynamic.views import app_views


app = Flask(__name__)
app.secret_key = "My Secret Key"
app.url_map.strict_slashes = False
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
