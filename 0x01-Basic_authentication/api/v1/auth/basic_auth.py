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

    def decode_base64_authorization_header(
        self, base64_authorization_header: str
    ) -> str:
        """Decodes base64 authorization base64 string"""

        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            b64_auth_header = base64_authorization_header.encode("utf-8")
            b64_auth_header = b64decode(b64_auth_header)
            b64_auth_header = b64_auth_header.decode("utf-8")
        except Exception as e:
            return None

        return b64_auth_header
