#!/usr/bin/env python3
"""
This module provides a function to hash passwords.
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    Arg: password - string; password to hash

    Return: the salted hashed password as a byte string
    """
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Arg1: hashed_password - bytes type; the hashed password
    Arg2: password - string type; the plain text password to check

    Return: boolean - True if password matches, else False
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
