#!/usr/bin/python3
"""DB module
"""
import bcrypt
from db import DB
from user import User


def _hash_password(password: str) -> bytes:
    """
    Method that takes in a password string arguments.
        Returns: Bytes. The returned bytes is a salted
        hash of the input password
    """
    bytePwd = password.encode('utf-8')
    mySalt = bcrypt.gensalt()
    return bcrypt.hashpw(bytePwd, mySalt)

class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """ Constructor
        """
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Method should take mandatory email and password string arguments.
            Returns: A User object.
        """
        if email and password:
            user = DB.find_user_by(email)
            if user is not None:
                raise ValueError("User {} already exists".format(email))
            print("user is None")
            hashed_password = _hash_password(password)
            hashed_password = str(hashed_password)
            print(hashed_password)
            print("hashed_password")
            new_user = self._db.add_user(email, hashed_password)
            return new_user
        return None
