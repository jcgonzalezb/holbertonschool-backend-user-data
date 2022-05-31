#!/usr/bin/python3
"""DB module
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """
    Method that takes in a password string arguments.
        Returns: Bytes. The returned bytes is a salted
        hash of the input password
    """
    bytePwd = password.encode('utf-8')
    mySalt = bcrypt.gensalt()
    return bcrypt.hashpw(bytePwd, mySalt)
