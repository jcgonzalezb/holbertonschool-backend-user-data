#!/usr/bin/env python3
"""
Class BasicAuth
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """flask authorization BasicAuth Class
    """

    def __init__(self):
        """ Constructor
        """
        super().__init__()

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        if authorization_header is None or not isinstance(
                authorization_header, str):
            return None

        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header[6:]
