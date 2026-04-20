from lms_app.models.user_model import User
from lms_app.extensions.db import db
from lms_app.auth.auth_utils import hash_password, verify_password, generate_token


# 📝 Register User
def register_user(name, email, password):
    try:
        # Check if user already exists
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return {"error": "User already exists"}, 400

        # Create new user
        new_user = User(
            name=name,
            email=email,
            password=hash_password(password)
        )

        db.session.add(new_user)
        db.session.commit()

        return {"message": "User registered successfully"}, 201

    except Exception as e:
        return {"error": str(e)}, 500


# 🔑 Login User
def login_user(email, password):
    try:
        user = User.query.filter_by(email=email).first()

        # Check user existence
        if not user:
            return {"error": "User not found"}, 404

        # Prevent password login for Google users
        if user.is_google_user:
            return {"error": "Please login using Google"}, 400

        # Verify password
        if not verify_password(password, user.password):
            return {"error": "Invalid credentials"}, 401

        # Generate token
        token = generate_token(user.id)

        return {
            "message": "Login successful",
            "token": token,
            "user": {
                "id": user.id,
                "email": user.email,
                "name": user.name
            }
        }, 200

    except Exception as e:
        return {"error": str(e)}, 500


# 🌐 Google Login (Basic - we’ll enhance later)
def google_login(email, name, profile_pic=None):
    try:
        user = User.query.filter_by(email=email).first()

        # If user doesn't exist → create
        if not user:
            user = User(
                name=name,
                email=email,
                is_google_user=True,
                profile_pic=profile_pic
            )
            db.session.add(user)
            db.session.commit()

        # Generate token
        token = generate_token(user.id)

        return {
            "message": "Google login successful",
            "token": token,
            "user": {
                "id": user.id,
                "email": user.email,
                "name": user.name
            }
        }, 200

    except Exception as e:
        return {"error": str(e)}, 500