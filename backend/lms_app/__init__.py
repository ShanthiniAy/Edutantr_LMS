import lms_app
from flask import Flask
from lms_app.config import Config
from lms_app.extensions.oauth_client import oauth

# Extensions
from lms_app.extensions.db import db

# Blueprints
from lms_app.auth.auth_routes import auth_bp
from lms_app.routes.health_check import health_bp


def create_app():
    app = Flask(__name__)

    # Load config
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    oauth.init_app(app)

    # Register blueprints
    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(health_bp, url_prefix="/api")

    return app