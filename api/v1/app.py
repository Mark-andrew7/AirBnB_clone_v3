#!/usr/bin/python3
"""
Status of api
"""

from flask import Flask, Blueprint, jsonify
from api.v1.views import app_views
from models import storage
from os import getenv


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_appcontext(self):
    """
    Closes the storage
    """
    storage.close()


@app.error_handler(404)
def error_handler(e):
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    host = getenv("HBNB_API_HOST", "0.0.0.0")
    port = int(getenv("HBNB_API_PORT", "5000"))
    app.run(host=host, port=port, threaded=True)
