from ..extensions import db
from ..models import Grade, User, Course

def student_grades(user_id: int):
    return Grade.query.filter_by(user_id=user_id).order_by(Grade.created_at.desc()).all()

def all_students():
    return User.query.filter_by(role="student").order_by(User.name.asc()).all()

def all_courses():
    return Course.query.order_by(Course.code.asc()).all()

def add_grade(student_id: int, course_id: int, item_name: str, score: float):
    g = Grade(user_id=student_id, course_id=course_id, item_name=item_name.strip(), score=float(score))
    db.session.add(g)
    db.session.commit()
    return g
