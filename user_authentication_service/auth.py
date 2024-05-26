#!/usr/bin/env python3
"""
Auth module
"""
import bcrypt

def _hash_password(password: str) -> bytes:
    """
    Arg1: password - str; the password to hash
    Return: bytes - the salted hash of the input password
    """
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed
