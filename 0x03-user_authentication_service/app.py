#!/usr/bin/env python3
"""
Route module for the API
"""
from flask import Flask, jsonify, request, abort, make_response, redirect
from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> str:
    """ GET /
    Return:
      - Welcome message.
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users() -> str:
    """ POST /users
    Function to create user
    Return:
    - User object JSON represented
    - 400 if the user is already registered
    """
    try:
        form = request.form
        email = form['email']
        password = form['password']
        new_user = AUTH.register_user(email, password)
        if new_user:
            return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    """ POST /sessions
    Function to log in a session
    Return:
    - A JSON payload of the form
    - 401 if the login information is incorrect
    """

    form = request.form
    email = form['email']
    password = form['password']
    valid_user = AUTH.valid_login(email, password)
    if valid_user:
        session_id = AUTH.create_session(email)
        message = jsonify({"email": email, "message": "logged in"})
        response = make_response(message)
        response.set_cookie("session_id", session_id)
        return response
    else:
        abort(401)


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout():
    """ DELETE /sessions
    Function to respond to the DELETE /sessions route.
    Return:
    - If the user exists destroy the session and redirect the user to '/'.
    - 403 if the user does not exist
    """
    form = request.form
    session_id = form['session_id']
    valid_user = AUTH.get_user_from_session_id(session_id=session_id)
    if valid_user:
        AUTH.destroy_session(valid_user.id)
        return redirect('/')
    else:
        abort(403)

    form = request.form
    email = form['email']
    password = form['password']
    valid_user = AUTH.valid_login(email, password)
    if valid_user:
        session_id = AUTH.create_session(email)
        message = jsonify({"email": email, "message": "logged in"})
        response = make_response(message)
        response.set_cookie("session_id", session_id)
        return response
    else:
        abort(401)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
