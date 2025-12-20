from __future__ import annotations # Add Students 

from flask import request

from . import api_bp
from .utils import ok, error, get_json_or_error
from ..extensions import db
from ..models import Student 

def _student_to_dict(s: Student) -> dict:
    return {
        "id": s.id,
        "name": getattr(s, "name", None),
        "email": getattr(s, "email", None),
    }


@api_bp.get("/students")
def list_students():
    students = Student.query.all()
    return ok([_student_to_dict(s) for s in students])


@api_bp.get("/students/<int:student_id>")
def get_student(student_id: int):
    s = Student.query.get(student_id)
    if not s:
        return error("Student not found", 404)
    return ok(_student_to_dict(s))


@api_bp.post("/students")
def create_student():
    data = get_json_or_error(required=True)
    if isinstance(data, tuple):
        return data 

    name = (data.get("name") or "").strip()
    email = (data.get("email") or "").strip().lower()

    if not name:
        return error("name is required", 400)
    if not email:
        return error("email is required", 400)

    exists = Student.query.filter_by(email=email).first()
    if exists:
        return error("email already exists", 409)

    s = Student(name=name, email=email)
    db.session.add(s)
    db.session.commit()
    return ok(_student_to_dict(s), 201)


@api_bp.put("/students/<int:student_id>")
def update_student(student_id: int):
    s = Student.query.get(student_id)
    if not s:
        return error("Student not found", 404)

    data = get_json_or_error(required=True)
    if isinstance(data, tuple):
        return data

    name = data.get("name")
    email = data.get("email")

    if name is not None:
        name = str(name).strip()
        if not name:
            return error("name cannot be empty", 400)
        s.name = name

    if email is not None:
        email = str(email).strip().lower()
        if not email:
            return error("email cannot be empty", 400)

        exists = Student.query.filter(Student.email == email, Student.id != s.id).first()
        if exists:
            return error("email already exists", 409)

        s.email = email

    db.session.commit()
    return ok(_student_to_dict(s))


@api_bp.delete("/students/<int:student_id>")
def delete_student(student_id: int):
    s = Student.query.get(student_id)
    if not s:
        return error("Student not found", 404)

    db.session.delete(s)
    db.session.commit()
    return ok({"deleted": True})
