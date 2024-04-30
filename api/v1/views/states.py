#!/usr/bin/python3
"""
new view for State objects that handles all default RESTFul API actions
"""

from api.v1.views import app_views
from models import storage
from models.state import State
from flask import jsonify, request, abort


@app_views.route("/states", methods=[GET])
def get_states():
    """
    Retrieves the list of all State objects
    """
    states = storage.all(State).values()
    states_list = []
    for state in states:
        states_list.append(state.to_dict())
    return jsonify(states_list)


@app_views.route("/states/<state_id>", methods=[GET])
def get_state():
    """
    Retrieves a state object
    """
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    return jsonify(state.to_dict())


@app_views.route("/states/<state_id>", methods=[DELETE])
def del_state():
    """
    Deletes a state object
    """
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    storage.delete(state)
    storage.save()
    return jsonify({}), 200


@app_views.route("/states", methods=[POST])
def create_state():
    """
    Creates a state object
    """
    if not request.json:
        abort(400, "Not a json")
    if "name" not in request.json:
        abort(400, "Missing name")
    data = request.json
    state = State(**data)
    storage.new(state)
    storage.save()
    return jsonify(state.to_dict())


@app_views.route("/states/<state_id>", methods=[PUT])
def update_state():
    """
    Updates a state object
    """
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    if not request.json():
        abort(400, "Not a json")
    data = request.json
    for k, v in data.items():
        if k not in ["id", "created_at", "updated_at"]:
            setattr(state, k, v)
    return jsonify(state.to_dict()), 200
