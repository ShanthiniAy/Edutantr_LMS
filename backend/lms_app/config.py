import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class Config:
    # 🔐 Secret key (used for JWT, sessions)
    SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")

    # 🗄️ Database configuration
    SQLALCHEMY_DATABASE_URI =  "sqlite:///lms.db"   # default for local development

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 🔑 JWT Configuration
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "jwt-secret-key")
    JWT_ACCESS_TOKEN_EXPIRES = 60 * 60 * 24  # 1 day (in seconds)

    # 🌐 Google OAuth (we’ll use later)
    GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
    GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")