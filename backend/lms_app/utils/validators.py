import re


# 📧 Validate Email
def validate_email(email):
    if not email:
        return False, "Email is required"

    email_regex = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    if not re.match(email_regex, email):
        return False, "Invalid email format"

    return True, None


# 🔐 Validate Password
def validate_password(password):
    if not password:
        return False, "Password is required"

    if len(password) < 6:
        return False, "Password must be at least 6 characters"

    return True, None


# 👤 Validate Name
def validate_name(name):
    if not name:
        return False, "Name is required"

    if len(name) < 2:
        return False, "Name must be at least 2 characters"

    return True, None