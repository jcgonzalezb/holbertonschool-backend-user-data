#!/usr/bin/python3
"""DB module
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.exc import NoResultFound


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
            try:
                find_user = self._db.find_user_by(email=email)
                if find_user is not None:
                    raise ValueError("User {} already exists".format(email))
            except NoResultFound:
                hashed_password = _hash_password(password)
                hashed_password = hashed_password.decode('utf8')
                new_user = self._db.add_user(email, hashed_password)
                return new_user
        return None

    def valid_login(self, email: str, password: str) -> bool:
        """
        Method should take mandatory email and password string arguments.
            Returns: A boolean.
        """
        if email and password:
            try:
                user = self._db.find_user_by(email=email)
                if user is None:
                    return False
                bytePwd = password.encode('utf-8')
                hashed_password = str(user.hashed_password)
                hashed_password = hashed_password.encode('utf-8')
                if not bcrypt.checkpw(bytePwd, hashed_password):
                    return False
                return True
            except NoResultFound:
                return False
