#!/usr/bin/python3
"""
Status of api
"""

from api.v1.views import app_views


@app_views.route("/status", methods=["GET"])
def status():
    """
    Returns status of api
    """
    return jsonify({"status": "OK"})
