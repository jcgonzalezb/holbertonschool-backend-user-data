#!/usr/bin/env python3
"""
Class BasicAuth
"""
from api.v1.auth.auth import Auth
from flask import request


class BasicAuth(Auth):
    """flask authorization BasicAuth Class
    """

    def __init__(self):
        """ Constructor
        """
        pass

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        if authorization_header is None or not isinstance(
                authorization_header, str):
            return None

        start_auth = authorization_header[:6]
        base64_auth = authorization_header[6:]

        if start_auth != "Basic ":
            return None
        return base64_auth
