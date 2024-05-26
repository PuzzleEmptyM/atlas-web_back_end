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
