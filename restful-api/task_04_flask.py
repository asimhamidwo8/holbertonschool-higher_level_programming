#!/usr/bin/env python3
"""
task_04_flask.py

A simple Flask-based API for the exercise.

Endpoints:
- GET /            -> Welcome message
- GET /data        -> JSON list of usernames
- GET /status      -> plain text OK
- GET /users/<username> -> user object or 404
- POST /add_user   -> add a user (expects JSON payload)

Note: users are stored in-memory in the `users` dict.
"""
from flask import Flask, jsonify, request
from typing import Dict

app = Flask(__name__)

# In-memory users store; keep empty by default to avoid shipping test data
users: Dict[str, Dict] = {}


@app.route("/", methods=["GET"])
def home():
    return "Welcome to the Flask API!"


@app.route("/data", methods=["GET"])
def get_data():
    # return list of usernames
    return jsonify(list(users.keys()))


@app.route("/status", methods=["GET"])
def status():
    return "OK"


@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    user = users.get(username)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)


@app.route("/add_user", methods=["POST"])
def add_user():
    # Parse JSON body safely
    data = None
    try:
        data = request.get_json(silent=True)
    except Exception:
        data = None

    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # Construct user object; ensure username is included
    user = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city"),
    }

    users[username] = user
    return jsonify({"message": "User added", "user": user}), 201


if __name__ == "__main__":
    # Run development server on port 5000
    app.run(host="0.0.0.0", port=5000)
