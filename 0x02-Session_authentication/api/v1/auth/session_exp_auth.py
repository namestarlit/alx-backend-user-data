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
        if not session_id:
            return
        session_dict = self.user_id_by_session_id.get(session_id, None)
        if session_dict:
            user = session_dict.get("user_id", None)
            if user:
                sd = self.session_duration
                if sd <= 0:
                    return user
                created_at = session_dict.get("created_at", None)
                if not created_at:
                    return
                if datetime.now() > created_at + timedelta(seconds=sd):
                    return
                return user
