#!/usr/bin/python3
"""
Status of api
"""
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route("/status", methods=["GET"])
def status():
    """
    Returns status of api
    """
    return jsonify({"status": "OK"})


@app_views.route("/api/v1/stats", methods=["GET"], strict_slashes=False)
def get_stats():
    """
    Retrives number of each object
    """
    classes = {
        "amenities": "Amenity",
        "cities": "City",
        "places": "Place",
        "reviews": "Review",
        "states": "State",
        "users": "User"
    }
    stats = {}
    for k, v in classes.items():
        stats[k] = storage.count(v)
    return jsonify(stats)
