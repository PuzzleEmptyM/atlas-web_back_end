#!/usr/bin/env python3
"""
Basic Authentication Module
"""
import base64
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """
    BasicAuth class that inherits from Auth
    """

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
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

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """
        Decodes the Base64 part of the Authorization header

        Arg: base64_authorization_header - str; Base64 encoded authorization
             header
        Return: str; decoded value as UTF-8 string, or None if invalid
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            return decoded_bytes.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """
        Extracts user email and password from the Base64 decoded value

        Arg: decoded_base64_authorization_header - str; decoded authorization
             header
        Return: (str, str); user email and password, (None, None) if invalid
        """
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None

        user_email, user_password = decoded_base64_authorization_header.split(
            ':', 1)
        return user_email, user_password
