#!/usr/bin/python3
"""DB module
"""
from gettext import find
from requests import session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError

from user import Base
from user import User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
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
        if email and hashed_password:
            user = User(
                email=email, hashed_password=hashed_password
            )
            self._session.add(user)
            self._session.commit()
            return user
        return None

    def find_user_by(self, **kwargs) -> User:
        """
        Method that takes in arbitrary keyword arguments.
            Returns: The first row found in the users table as filtered
        by the passed arguments.
        """
        valid_arguments = [
            'id', 'email', 'hashed_password', 'session_id', 'reset_token'
        ]
        input_keys = kwargs.keys()
        for k in input_keys:
            if k not in valid_arguments:
                raise InvalidRequestError
            user = self._session.query(User).filter_by(**kwargs).first()
            if user is None:
                raise NoResultFound
            return user

    def update_user(self, user_id = int, **kwargs) -> None:
        """
        Method that takes as argument a required user_id integer
        and arbitrary keyword arguments.
            Returns: None.
        """
        valid_arguments = [
            'id', 'email', 'hashed_password', 'session_id', 'reset_token'
        ]
        input_keys = kwargs.keys()
        user_located = self.find_user_by(id=user_id)
        for k in input_keys:
            if k not in valid_arguments:
                raise ValueError
            user_located.k = kwargs.values()
            self._session.commit()
            return None
