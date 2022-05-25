#!/usr/bin/env python3
"""
Class SessionAuth
"""
from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """flask authorization SessionAuth Class
    """

    def __init__(self):
        """ Constructor
        """
        super().__init__()
