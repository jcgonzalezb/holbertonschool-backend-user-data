#!/usr/bin/env python3
""" Module Flask view that handles all routes for the Session authentication.
"""
from flask import jsonify, request
from api.v1.views import app_views
from models.user import User
from typing import TypeVar

@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """ POST /auth_session/login
    Return:
      - Access to user
    """
    email = request.form.get('email')
    password = request.form.get('password')
    if email == '' or None:
      return jsonify({"error": "email missing"}), 400
    if password == '' or None:
      return jsonify({"error": "password missing"}), 400
    
    user_credentials = {'email': email, }
    user = User()
    result = user.search(user_credentials)
    if not result:
        return jsonify({ "error": "no user found for this email" }), 404
    user = result[0]
    if not user.is_valid_password(password):
        return jsonify({ "error": "wrong password" }), 401
