#!/usr/bin/env python3
""" Module Flask view that handles all routes for the Session authentication.
"""
from flask import jsonify, abort


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login() -> str:
    """ POST /auth_session/login
    Return:
      - the status of the API
    """





    
    return jsonify({"status": "OK"})
