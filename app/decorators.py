from functools import wraps
from flask import redirect, url_for, flash
from .auth.services import get_current_user

def login_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if not get_current_user():
            flash("Please login first.", "warning")
            return redirect(url_for("auth.login"))
        return fn(*args, **kwargs)
    return wrapper

def role_required(role: str):
    def deco(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            u = get_current_user()
            if not u or u.role != role:
                flash("Access denied.", "danger")
                return redirect(url_for("dashboard.dashboard"))
            return fn(*args, **kwargs)
        return wrapper
    return deco
