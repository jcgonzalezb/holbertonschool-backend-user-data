#!/usr/bin/env python3
"""
Contains DB class to handle data.
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from user import Base, User


class DB():
    """
    DB class to handle data
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db")
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Set and Return the user session.
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
        Method that takes two arguments to save the user to the database.
            Returns: A User object.
        """
        if email is None or not isinstance(email, str):
            return None
        if hashed_password is None or not isinstance(hashed_password, str):
            return None
        new_user = User(email=email, hashed_password=hashed_password)
        self._session.add(new_user)
        self._session.commit()
        return new_user
