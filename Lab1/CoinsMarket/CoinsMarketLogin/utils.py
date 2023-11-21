from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password, ValidationError
from email_validator import validate_email, EmailNotValidError
import re


def validate_signup_info(username, password, email):
    try:
        validate_password(password)
    except ValidationError:
        return "Password should be at least 8 characters long"
    if User.objects.filter(username=username).exists():
        return "User with such username already exists"
    if User.objects.filter(email=email).exists():
        return "User with such email already exists"
    try:
        validate_email(email)
    except EmailNotValidError as e:
        return "Email is not valid"
    if not re.match("^[A-Za-z0-9_-]*$", username):
        return "Username can only contain letters, numbers, underscores and dashes"
    return ""
