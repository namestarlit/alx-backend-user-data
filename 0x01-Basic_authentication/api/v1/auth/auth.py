#!/usr/bin/env python3
"""Authentication module"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Auth class implementantion"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Require authentication method"""

        if path is None:
            return True
        if excluded_paths is None or excluded_paths == []:
            return True
        if path in excluded_paths:
            return False

        for excluded_path in excluded_paths:
            if excluded_path.startswith(path):
                return False
            elif path.startswith(excluded_path):
                return False
            elif excluded_path[-1] == "*":
                if path.startswith(excluded_path[:-1]):
                    return False

        return True

    def authorization_header(self, request=None) -> str:
        """Authorization header"""

        if request is None:
            return None
        if "Authorization" not in request.headers:
            return None

        return request.headers["Authorization"]

    def current_user(self, request=None) -> TypeVar("User"):
        """Current user"""
        return None
