#!/usr/bin/env python3
"""
Route module for the API
"""
from flask import Flask, jsonify
from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'], strict_slashes=False)
def home() -> str:
    """ GET /
    Return:
      - Welcome message.
    """
    return jsonify({"message": "Bienvenue"})

@app.route('/users', methods=['POST'], strict_slashes=False)
def users() -> str:
    """ POST /users
    JSON body:
    - email
    - password
    - last_name (optional)
    - first_name (optional)
    Return:
    - User object JSON represented
    - 400 if can't create the new User
    """
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
