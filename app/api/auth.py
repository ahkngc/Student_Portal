from flask_login import login_user, logout_user
from . import api_bp
from .utils import ok, error, get_json_or_error
from ..models import User


@api_bp.post("/auth/login")
def login():
    data = get_json_or_error(required=True)
    if isinstance(data, tuple):
        return data

    email = data.get("email")
    password = data.get("password")

    user = User.query.filter_by(email=email).first()
    if not user or not user.check_password(password):
        return error("Invalid credentials", 401)

    login_user(user)
    return ok({"role": user.role})


@api_bp.post("/auth/logout")
def logout():
    logout_user()
    return ok({"logged_out": True})
