#!/usr/bin/env python3
"""
This module provide flask class
"""
from flask import Flask, jsonify, request


app = Flask(__name__)


users = {
    "jane": {
        "username": "Jane",
        "name": "Jane",
        "age": 28,
        "city": "Los Angeles"}
}


@app.route('/')
def home():
    return "Welcome to the Flask API!"


@app.route("/data")
def print_data():
    return jsonify([key for key in users])


@app.route("/status")
def print_status():
    return "OK"


@app.route("/users/<username>")
def print_profile(username):
    user = users.get(username)
    if user:
        ordered_user = [(key, user[key]) for key in user]
        return jsonify(dict(ordered_user))
    return jsonify({"error": "User not found"})


@app.route("/add_user", methods=['POST'])
def add_user():
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
