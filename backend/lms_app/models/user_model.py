from datetime import datetime
from lms_app.extensions.db import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    # Basic Info
    name = db.Column(db.String(100), nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=True)

    # Auth Type
    is_google_user = db.Column(db.Boolean, default=False)

    # Optional (for Google login / profile)
    profile_pic = db.Column(db.String(255), nullable=True)

    # Role (future use: admin, student, instructor)
    role = db.Column(db.String(50), default="student")

    # Status
    is_active = db.Column(db.Boolean, default=True)

    # Timestamps
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<User {self.email}>"