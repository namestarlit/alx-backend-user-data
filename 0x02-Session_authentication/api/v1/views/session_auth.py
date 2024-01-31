#!/usr/bin/env python3
"""Session auth views"""
import os
from models.user import User
from api.v1.views import app_views
from flask import jsonify, request, abort


@app_views.route("/ath_session/login", methods=["POST"], strict_slashes=False)
def auth_session():
    """auth session"""
    email = request.form.get("email")
    password = request.form.get("password")

    if email is None or email == "":
        return jsonify({"error": "email missing"}), 400
    if password is None or password == "":
        return jsonify({"error": "no user found for this email"}), 404
    for user in users:
        if user.is_valid_password(password):
            from api.v1.app import auth

            session_id = auth.create_session(user.id)
            resp = jsonify(user.to_json())
            session_name = os.getenv("SESSION_NAME")
            resp.set_cookie(session_name, session_id)
            return resp

    return jsonify({"error": "wrong password"}), 401


@app_views.route(
    "/auth_session/logout", methods=["DELETE"], strict_slashes=False
)
def logout():
    """Logout user"""
    from api.v1.app import auth

    if auth.destroy_session(request):
        return jsonify({}), 200
    abort(404)
