#!/usr/bin/env python3
"""
API Authentication Module
"""
from flask import request
from typing import List, TypeVar
from os import getenv


class Auth:
    """
    Class to manage the API authentication
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if a path requires authentication
        Arg1: path - str; The path to check
        Arg2: excluded_paths - str; list of paths that don't require auth
        Return: bool; True if authentication is required, False otherwise
        """
        if path is None:
            return True

        if excluded_paths is None or len(excluded_paths) == 0:
            return True

        if path[-1] != '/':
            path += '/'

        for excluded_path in excluded_paths:
            if excluded_path[-1] != '/':
                excluded_path += '/'
            if path == excluded_path:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        Returns the authorization header from the request
        Arg: request - Flask request object; The Flask request object
        Return: str - The authorization header, or None if not present
        """
        if request is None:
            return None

        return request.headers.get('Authorization', None)

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Returns the current user from the request
        Arg: request - Flask request object; The Flask request object
        Return: TypeVar; The current user, or None if not present
        """
        return None

    def session_cookie(self, request=None):
        """
        Returns the value of the session cookie from the request
        Arg: request - Flask request object; The Flask request object
        Return: str - The value of the session cookie, or None if not present
        """
        if request is None:
            return None

        session_name = getenv('SESSION_NAME')
        if session_name is None:
            return None

        return request.cookies.get(session_name)
