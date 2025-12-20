from flask import session
from ..models import User
from ..utils import normalize_email

SESSION_USER_ID = "user_id"

def login_user(email: str, password: str):
    email = normalize_email(email)
    u = User.query.filter_by(email=email).first()
    if not u or not u.check_password(password):
        return None
    session[SESSION_USER_ID] = u.id
    return u

def logout_user():
    session.pop(SESSION_USER_ID, None)

def get_current_user():
    uid = session.get(SESSION_USER_ID)
    return User.query.get(uid) if uid else None
