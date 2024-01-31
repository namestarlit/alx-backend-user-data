#!/usr/bin/env python3
"""Session expiration module"""
from os import getenv
from datetime import datetime, timedelta
from api.v1.auth.session_auth import SessionAuth


class SessionExpAuth(SessionAuth):
    """SessionExpAuth class"""

    def __init__(self):
        """initialize SessionExpAuth class attributes"""
        super().__init__()
        self.session_duration = int(getenv("SESSION_DURATION", 0))

    def create_session(self, user_id=None):
        """create a session ID with expiration time"""
        session_id = super().create_session(user_id)
        if session_id is None:
            return None

        session_dict = {"user_id": user_id, "created_at": datetime.now()}
        self.user_id_by_session_id[session_id] = session_dict
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """Retrives user_id for session ID"""
        if session_id is None or "created_at" not in self.user_id_by_session_id:
            return None

        session_dict = self.user_id_by_session_id[session_id]
        if self.session_duration <= 0 or "created_at" not in session_dict:
            return session_dict.get("user_id")

        created_a = session_dict["created_at"]
        expiration_time = created_at + timedelta(seconds=self.session_duration)

        if expiration_time < datetime.now():
            return None

        return session_dict.get("user_id")
