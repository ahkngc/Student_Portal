from __future__ import annotations

from . import api_bp
from .utils import ok, error, get_json_or_error
from ..extensions import db
from ..models import Enrollment, Student, Course


def _enrollment_to_dict(e: Enrollment) -> dict:
    return {
        "id": e.id,
        "student_id": e.student_id,
        "course_id": e.course_id,
    }


@api_bp.get("/enrollments")
def list_enrollments():
    enrollments = Enrollment.query.all()
    return ok([_enrollment_to_dict(e) for e in enrollments])


@api_bp.post("/enrollments")
def create_enrollment():
    data = get_json_or_error(required=True)
    if isinstance(data, tuple):
        return data

    student_id = data.get("student_id")
    course_id = data.get("course_id")

    if not student_id or not course_id:
        return error("student_id and course_id are required", 400)

    student = Student.query.get(student_id)
    if not student:
        return error("Student not found", 404)

    course = Course.query.get(course_id)
    if not course:
        return error("Course not found", 404)

    exists = Enrollment.query.filter_by(
        student_id=student_id,
        course_id=course_id
    ).first()

    if exists:
        return error("Student already enrolled in this course", 409)

    enrollment = Enrollment(
        student_id=student_id,
        course_id=course_id
    )
    db.session.add(enrollment)
    db.session.commit()

    return ok(_enrollment_to_dict(enrollment), 201)


@api_bp.delete("/enrollments/<int:enrollment_id>")
def delete_enrollment(enrollment_id: int):
    enrollment = Enrollment.query.get(enrollment_id)
    if not enrollment:
        return error("Enrollment not found", 404)

    db.session.delete(enrollment)
    db.session.commit()

    return ok({"deleted": True})
