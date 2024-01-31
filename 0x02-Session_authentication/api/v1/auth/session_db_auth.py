#!/usr/bin/env python3
"""Database session authentication"""
from datetime import datetime, timedelta
from models.user_session import UserSession
from api.v1.auth.session_exp_auth import SessionExpAuth


class SessionDBAuth(SessionExpAuth):
    """SessionDBAuth class"""

    def create_session(self, usr_id=None):
        """Create session Id and store in the database"""
        session_id = super().create_session(user_id)
        if session_id is None:
            return None

        session = UserSession(user_id=user_id, session_id=session_id)
        session.save()

        return session_id

    def user_id_for_session_id(self, session_id=None):
        """Retrive user_id for session from database"""
        if session_id is None:
            return None

        session = UserSession.search({"session_id": session_id})
        if not session:
            return None

        session = session[0]
        if (
            self.session_duration > 0
            and session.created_at + timedelta(seconds=self.session_duration)
            < datetime.now()
        ):
            return None

        return session.user_id

    def destroy_session(self, request=None):
        """Destroy the user session"""
        if request is not None:
            session_id = self.session_cookie(request)
            if session_id:
                sessions = UserSession.search({"session_id": session_id})
                if sessions:
                    for session in sessions:
                        session.remove()
