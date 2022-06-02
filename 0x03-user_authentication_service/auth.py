#!/usr/bin/env python3
"""
Class Auth
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
import uuid
from typing import Union


def _hash_password(password: str) -> bytes:
    """
    Method that takes in a password string arguments.
        Returns: Bytes. The returned bytes is a salted
        hash of the input password
    """
    bytePwd = password.encode('utf-8')
    mySalt = bcrypt.gensalt()
    return bcrypt.hashpw(bytePwd, mySalt)


def _generate_uuid() -> str:
    """
    Method doesn't take arguments.
        Returns: A string representation of a new UUID.
    """
    return str(uuid.uuid4())


class Auth():
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
        return None

    def create_session(self, email: str) -> str:
        """
        Method takes an email string argument.
            Returns: Session ID as a string.
        """
        if email:
            try:
                user = self._db.find_user_by(email=email)
                if user:
                    session_id = _generate_uuid()
                    self._db.update_user(user.id, session_id=session_id)
                    return session_id
            except NoResultFound:
                return None
        return None

    def get_user_from_session_id(self, session_id: str) -> str:
        """
        Method takes a single session_id string argument.
            Returns: The corresponding User or None.
        """
        if session_id is None:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None
