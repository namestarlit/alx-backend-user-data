#!/usr/bin/env python3
"""Authentication module"""
from flask import request
from base64 import b64decode
from typing import List, TypeVar

from models.user import User
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """BasicAuth class implementantion"""

    def extract_base64_authorization_header(
        self, authorization_header: str
    ) -> str:
        """Extracts the base64 string from the auth header"""
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        token = authorization_header.split(" ")[-1]

        if token:
            return token
        return None
