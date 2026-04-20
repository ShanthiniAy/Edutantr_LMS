from functools import wraps
from flask import request, jsonify
from lms_app.auth.auth_utils import decode_token
from lms_app.models.user_model import User


# 🔐 Decorator to protect routes
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        # 📥 Get token from headers
        if "Authorization" in request.headers:
            auth_header = request.headers["Authorization"]

            # Format: Bearer <token>
            if auth_header.startswith("Bearer "):
                token = auth_header.split(" ")[1]

        if not token:
            return jsonify({"error": "Token is missing"}), 401

        # 🔓 Decode token
        data = decode_token(token)

        if "error" in data:
            return jsonify(data), 401

        # 👤 Get user from DB
        user = User.query.get(data["user_id"])

        if not user:
            return jsonify({"error": "User not found"}), 404

        # Attach user to request
        request.current_user = user

        return f(*args, **kwargs)

    return decorated