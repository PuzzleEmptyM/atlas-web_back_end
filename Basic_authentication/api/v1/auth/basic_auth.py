#!/usr/bin/env python3
"""
Basic Authentication Module
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """
    BasicAuth class that inherits from Auth
    """

    def extract_base64_authorization_header(self, authorization_header: str)\
        -> str:
        """
        Extracts Base64 part of Authorization header for Basic Authentication
        Arg: authorization_header - str; authorization header
        Return: str; Base64 part of Authorization header, or None if invalid
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None

        return authorization_header[len("Basic "):]
