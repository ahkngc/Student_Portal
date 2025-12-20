from flask import Blueprint, render_template, redirect, url_for, request, flash
from ..decorators import login_required, role_required
from ..auth.services import get_current_user
from .services import list_courses, enrolled_course_ids, enroll, unenroll, create_course

bp = Blueprint("courses", __name__, url_prefix="/courses")

@bp.get("")
@login_required
def courses_page():
    user = get_current_user()
    courses = list_courses()
    ids = enrolled_course_ids(user.id) if user.role == "student" else set()
    return render_template("courses.html", user=user, courses=courses, enrolled_ids=ids)

@bp.post("/enroll")
@login_required
def enroll_route():
    user = get_current_user()
    if user.role != "student":
        flash("Only students can enroll.", "warning")
        return redirect(url_for("courses.courses_page"))

    ok = enroll(user.id, int(request.form["course_id"]))
    flash("Enrolled successfully!" if ok else "Already enrolled.", "success" if ok else "warning")
    return redirect(url_for("courses.courses_page"))

@bp.post("/unenroll")
@login_required
def unenroll_route():
    user = get_current_user()
    if user.role != "student":
        flash("Only students can unenroll.", "warning")
        return redirect(url_for("courses.courses_page"))

    ok = unenroll(user.id, int(request.form["course_id"]))
    flash("Unenrolled." if ok else "Not enrolled.", "info" if ok else "warning")
    return redirect(url_for("courses.courses_page"))

@bp.post("/create")
@login_required
@role_required("instructor")
def create_course_route():
    create_course(request.form["code"], request.form["title"])
    flash("Course created.", "success")
    return redirect(url_for("courses.courses_page"))
