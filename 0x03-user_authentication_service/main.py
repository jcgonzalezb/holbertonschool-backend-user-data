#!/usr/bin/env python3
"""
Contains main module
"""

import requests
import json


url = 'http://0.0.0.0:5000'


def register_user(email: str, password: str) -> None:
    """ Asserts this function's corresponding API route. """
    data = {'email': email, 'password': password}
    response = requests.post(url + '/users', data=data)
    assert response.status_code == 200


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


if __name__ == "__main__":

    register_user(EMAIL, PASSWD)
