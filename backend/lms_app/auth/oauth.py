from flask import Blueprint, redirect, url_for, session
from lms_app.extensions.oauth_client import oauth
from lms_app.auth.auth_service import google_login
from flask import current_app

oauth_bp = Blueprint("oauth", __name__)


# 🔹 Register Google OAuth
google = oauth.register(
    name="google",
    client_id=current_app.config["GOOGLE_CLIENT_ID"],
    client_secret=current_app.config["GOOGLE_CLIENT_SECRET"],
    server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
    client_kwargs={
        "scope": "openid email profile"
    }
)


# 🔹 Step 1: Redirect to Google
@oauth_bp.route("/login/google")
def login_with_google():
    redirect_uri = url_for("oauth.google_callback", _external=True)
    return google.authorize_redirect(redirect_uri)


# 🔹 Step 2: Callback from Google
@oauth_bp.route("/callback/google")
def google_callback():
    token = google.authorize_access_token()
    user_info = google.parse_id_token(token)

    email = user_info.get("email")
    name = user_info.get("name")
    picture = user_info.get("picture")

    # Use existing service
    response, status = google_login(email, name, picture)

    return response, status