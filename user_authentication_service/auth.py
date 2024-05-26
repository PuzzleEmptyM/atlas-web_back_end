#!/usr/bin/env python3
"""
Auth module
"""
import bcrypt
import uuid
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """
    Arg1: password - str; the password to hash
    Return: bytes - the salted hash of the input password
    """
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed


def _generate_uuid() -> str:
    """
    Return: str - string representation of a new UUID
    """
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Arg1: email - str; the email of the user to register
        Arg2: password - str; the password of the user to register
        Return: User - newly created User object or
                       raises ValueError if user already exists
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_password = _hash_password(password)
            user = self._db.add_user(email, hashed_password.decode())
            return user

    def valid_login(self, email: str, password: str) -> bool:
        """
        Arg1: email - str; the email of the user
        Arg2: password - str; the password of the user
        Return: bool - True if login is valid, else False
        """
        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(password.encode(),
                                  user.hashed_password.encode())
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """
        Arg1: email - str; the email of the user
        Return: str - the session ID for the user, or None if user is not found
        """
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except NoResultFound:
            return None
