from flask import Flask, jsonify
from flask_geo import Geolocation, geolocate_city


app = Flask(__name__)
Geolocation(app)


@app.route('/')
def index():
    return jsonify(geolocate_city())