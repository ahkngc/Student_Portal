from ..extensions import db
from ..models import Course, Enrollment

def list_courses():
    return Course.query.order_by(Course.code.asc()).all()

def enrolled_course_ids(user_id: int):
    return {e.course_id for e in Enrollment.query.filter_by(user_id=user_id).all()}

def enroll(user_id: int, course_id: int):
    if Enrollment.query.filter_by(user_id=user_id, course_id=course_id).first():
        return False
    db.session.add(Enrollment(user_id=user_id, course_id=course_id))
    db.session.commit()
    return True

def unenroll(user_id: int, course_id: int):
    e = Enrollment.query.filter_by(user_id=user_id, course_id=course_id).first()
    if not e:
        return False
    db.session.delete(e)
    db.session.commit()
    return True

def create_course(code: str, title: str):
    c = Course(code=code.strip().upper(), title=title.strip())
    db.session.add(c)
    db.session.commit()
    return c
