from flask import Blueprint, render_template
from ..decorators import login_required
from ..auth.services import get_current_user
from .services import student_dashboard, instructor_dashboard

bp = Blueprint("dashboard", __name__, url_prefix="/dashboard")

@bp.get("")
@login_required
def dashboard():
    user = get_current_user()
    if user.role == "student":
        data = student_dashboard(user.id)
        return render_template("dashboard.html", user=user, role=user.role, **data)

    data = instructor_dashboard()
    return render_template("dashboard.html", user=user, role=user.role, **data)
