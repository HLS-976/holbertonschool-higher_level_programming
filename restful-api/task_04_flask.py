#!/usr/bin/env python3
"""
This module provide flask class
"""
from flask import Flask, jsonify, request


app = Flask(__name__)


users = {}

@app.route('/')
def home():
    """
    This function print home message
    """
    return "Welcome to the Flask API!"


@app.route("/data")
def print_data():
    """
    This return data
    """
    return jsonify([key for key in users])


@app.route("/status")
def print_status():
    """
    This function return status
    """
    return "OK"


@app.route("/users/<username>")
def print_profile(username):
    """
    This function return profile
    """
    user = users.get(username)
    if user:
        ordered_user = dict([(key, user[key]) for key in user])
        return jsonify(ordered_user)
    return jsonify({"error": "User not found"})


@app.route("/add_user", methods=['POST'])
def add_user():
    """
    This function return user added
    """
    data = request.get_json()

    if not data or "username" not in data:
        return jsonify({"error": "Missing username"})

    username = data["username"]

    if username in users:
        return jsonify({"error": "User already exists"})

    users[username] = {
        "username": username,
        "name": data.get("name", ""),
        "age": data.get("age", 0),
        "city": data.get("city", "")}


if __name__ == "__main__":
    app.run()
