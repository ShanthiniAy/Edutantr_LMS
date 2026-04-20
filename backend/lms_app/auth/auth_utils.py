from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
from flask import current_app


# 🔒 Hash Password
def hash_password(password):
    return generate_password_hash(password)


# 🔍 Verify Password
def verify_password(password, hashed_password):
    return check_password_hash(hashed_password, password)


# 🎫 Generate JWT Token
def generate_token(user_id):
    payload = {
        "user_id": user_id,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(
            seconds=current_app.config["JWT_ACCESS_TOKEN_EXPIRES"]
        ),
        "iat": datetime.datetime.utcnow()
    }

    token = jwt.encode(
        payload,
        current_app.config["JWT_SECRET_KEY"],
        algorithm="HS256"
    )

    return token


# 🔓 Decode JWT Token
def decode_token(token):
    try:
        payload = jwt.decode(
            token,
            current_app.config["JWT_SECRET_KEY"],
            algorithms=["HS256"]
        )
        return payload
    except jwt.ExpiredSignatureError:
        return {"error": "Token expired"}
    except jwt.InvalidTokenError:
        return {"error": "Invalid token"}