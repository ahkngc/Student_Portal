from flask import Blueprint, render_template, redirect, url_for, request, flash
from ..decorators import login_required, role_required
from ..auth.services import get_current_user
from .services import list_announcements, create_announcement

bp = Blueprint("announcements", __name__, url_prefix="/announcements")

@bp.get("")
@login_required
def announcements_page():
    user = get_current_user()
    return render_template("announcements.html", user=user, items=list_announcements())

@bp.post("/create")
@login_required
@role_required("instructor")
def create_announcement_route():
    create_announcement(request.form["title"], request.form["body"])
    flash("Announcement posted.", "success")
    return redirect(url_for("announcements.announcements_page"))
