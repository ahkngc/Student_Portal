from __future__ import annotations

from . import api_bp
from .utils import ok, error, get_json_or_error
from ..extensions import db
from ..models import Grade, Enrollment


def _grade_to_dict(g: Grade) -> dict:
    return {
        "id": g.id,
        "enrollment_id": g.enrollment_id,
        "value": g.value,
    }


@api_bp.get("/grades")
def list_grades():
    grades = Grade.query.all()
    return ok([_grade_to_dict(g) for g in grades])


@api_bp.post("/grades")
def create_grade():
    data = get_json_or_error(required=True)
    if isinstance(data, tuple):
        return data

    enrollment_id = data.get("enrollment_id")
    value = data.get("value")

    if enrollment_id is None or value is None:
        return error("enrollment_id and value are required", 400)

    enrollment = Enrollment.query.get(enrollment_id)
    if not enrollment:
        return error("Enrollment not found", 404)

    try:
        value = float(value)
    except ValueError:
        return error("Grade value must be a number", 400)

    if value < 0 or value > 100:
        return error("Grade value must be between 0 and 100", 400)

    grade = Grade(
        enrollment_id=enrollment_id,
        value=value
    )
    db.session.add(grade)
    db.session.commit()

    return ok(_grade_to_dict(grade), 201)


@api_bp.patch("/grades/<int:grade_id>")
def update_grade(grade_id: int):
    grade = Grade.query.get(grade_id)
    if not grade:
        return error("Grade not found", 404)

    data = get_json_or_error(required=True)
    if isinstance(data, tuple):
        return data

    value = data.get("value")
    if value is None:
        return error("value is required", 400)

    try:
        value = float(value)
    except ValueError:
        return error("Grade value must be a number", 400)

    if value < 0 or value > 100:
        return error("Grade value must be between 0 and 100", 400)

    grade.value = value
    db.session.commit()

    return ok(_grade_to_dict(grade))
