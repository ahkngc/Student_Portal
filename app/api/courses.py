from __future__ import annotations

from . import api_bp
from .utils import ok, error, get_json_or_error
from ..extensions import db
from ..models import Course


def _course_to_dict(c: Course) -> dict:
    return {
        "id": c.id,
        "code": c.code,
        "name": c.name,
    }


@api_bp.get("/courses")
def list_courses():
    courses = Course.query.all()
    return ok([_course_to_dict(c) for c in courses])


@api_bp.get("/courses/<int:course_id>")
def get_course(course_id: int):
    course = Course.query.get(course_id)
    if not course:
        return error("Course not found", 404)
    return ok(_course_to_dict(course))


@api_bp.post("/courses")
def create_course():
    data = get_json_or_error(required=True)
    if isinstance(data, tuple):
        return data

    code = (data.get("code") or "").strip().upper()
    name = (data.get("name") or "").strip()

    if not code:
        return error("code is required", 400)
    if not name:
        return error("name is required", 400)

    exists = Course.query.filter_by(code=code).first()
    if exists:
        return error("Course code already exists", 409)

    course = Course(code=code, name=name)
    db.session.add(course)
    db.session.commit()

    return ok(_course_to_dict(course), 201)


@api_bp.put("/courses/<int:course_id>")
def update_course(course_id: int):
    course = Course.query.get(course_id)
    if not course:
        return error("Course not found", 404)

    data = get_json_or_error(required=True)
    if isinstance(data, tuple):
        return data

    if "code" in data:
        code = data["code"].strip().upper()
        if not code:
            return error("code cannot be empty", 400)

        exists = Course.query.filter(
            Course.code == code,
            Course.id != course.id
        ).first()
        if exists:
            return error("Course code already exists", 409)

        course.code = code

    if "name" in data:
        name = data["name"].strip()
        if not name:
            return error("name cannot be empty", 400)
        course.name = name

    db.session.commit()
    return ok(_course_to_dict(course))


@api_bp.delete("/courses/<int:course_id>")
def delete_course(course_id: int):
    course = Course.query.get(course_id)
    if not course:
        return error("Course not found", 404)

    db.session.delete(course)
    db.session.commit()
    return ok({"deleted": True})
