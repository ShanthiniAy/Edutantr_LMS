from flask import Blueprint, request, jsonify
from lms_app.auth.auth_service import register_user, login_user, google_login
from lms_app.utils.validators import validate_email, validate_password, validate_name

# Create Blueprint
auth_bp = Blueprint("auth", __name__)


# 📝 Register API
# 📝 Register API
@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    # 🔹 Basic check
    if not name or not email or not password:
        return jsonify({"error": "All fields are required"}), 400

    # 🔹 Name validation
    valid, error = validate_name(name)
    if not valid:
        return jsonify({"error": error}), 400

    # 🔹 Email validation
    valid, error = validate_email(email)
    if not valid:
        return jsonify({"error": error}), 400

    # 🔹 Password validation
    valid, error = validate_password(password)
    if not valid:
        return jsonify({"error": error}), 400

    # 🔹 Call service layer
    response, status = register_user(name, email, password)

    return jsonify(response), status


# 🔑 Login API
@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    email = data.get("email")
    password = data.get("password")

    # 🔹 Basic check
    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400

    # 🔹 Email validation
    valid, error = validate_email(email)
    if not valid:
        return jsonify({"error": error}), 400

    # 🔹 Call service layer
    response, status = login_user(email, password)

    return jsonify(response), status

# 🌐 Google Login API (frontend will send Google user data)
@auth_bp.route("/google-login", methods=["POST"])
def google_auth():
    data = request.get_json()

    email = data.get("email")
    name = data.get("name")
    profile_pic = data.get("profile_pic")

    if not email or not name:
        return jsonify({"error": "Invalid Google data"}), 400

    response, status = google_login(email, name, profile_pic)
    return jsonify(response), status