#!/usr/bin/env python3
"""
Class SessionAuth
"""
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """flask authorization SessionAuth Class
    """
    user_id_by_session_id = {}

    def __init__(self):
        """ Constructor
        """
        super().__init__()

    def create_session(self, user_id: str = None) -> str:
        """
        This instance method that creates a Session ID for a user_id.
        """
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        This instance method that returns a User ID based on a Session ID:
        """
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)
