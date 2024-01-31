#!/usr/bin/env python3
"""Database session module"""
from models.base import Base
from sqlalchemy import Column, Strin, ForeignKey


class UserSession(Base):
    """UserSession class"""

    __tablename__ = "user_sessions"
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    session_id = Column(String(60), nullable=False)
