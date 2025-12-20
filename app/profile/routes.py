from flask import Blueprint, render_template, redirect, url_for, request, flash
from ..decorators import login_required
from ..auth.services import get_current_user
from .services import change_password

bp = Blueprint("profile", __name__, url_prefix="/profile")

@bp.get("")
@login_required
def profile_page():
    user = get_current_user()
    return render_template("profile.html", user=user)

@bp.post("/change-password")
@login_required
def change_password_route():
    user = get_current_user()
    new_pw = request.form.get("new_password", "")
    if len(new_pw.strip()) < 4:
        flash("Password must be at least 4 characters.", "warning")
        return redirect(url_for("profile.profile_page"))
    change_password(user, new_pw)
    flash("Password updated.", "success")
    return redirect(url_for("profile.profile_page"))
