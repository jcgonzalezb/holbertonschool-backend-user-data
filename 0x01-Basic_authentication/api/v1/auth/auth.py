#!/usr/bin/env python3
"""
Class Auth
"""
from flask import request

class Auth():
    """flask authorization Auth Class
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Public method that requires authentication
            Returns: False - path and excluded_paths
        """
        return 
    
    def authorization_header(self, request=None) -> str:
        """Public method that requires authentication
            Returns: False - path and excluded_paths
        """
        return
    
    def current_user(self, request=None) -> TypeVar('User'):
        """Public method that requires authentication
            Returns: False - path and excluded_paths
        """
        return




