from flask import Blueprint, render_template, redirect, url_for, request, flash
from ..decorators import login_required, role_required
from ..auth.services import get_current_user
from .services import student_grades, all_students, all_courses, add_grade

bp = Blueprint("grades", __name__, url_prefix="/grades")

@bp.get("")
@login_required
def grades_page():
    user = get_current_user()
    if user.role == "student":
        return render_template("grades.html", user=user, role=user.role, grades=student_grades(user.id))
    return render_template("grades.html", user=user, role=user.role, students=all_students(), courses=all_courses())

@bp.post("/add")
@login_required
@role_required("instructor")
def add_grade_route():
    add_grade(
        int(request.form["student_id"]),
        int(request.form["course_id"]),
        request.form["item_name"],
        float(request.form["score"]),
    )
    flash("Grade added.", "success")
    return redirect(url_for("grades.grades_page"))
