from ..models import Course, Grade, Announcement, Enrollment, User

def student_dashboard(user_id: int):
    enrolled = Enrollment.query.filter_by(user_id=user_id).count()
    recent_grades = Grade.query.filter_by(user_id=user_id).order_by(Grade.created_at.desc()).limit(5).all()
    recent_ann = Announcement.query.order_by(Announcement.created_at.desc()).limit(3).all()
    return {
        "enrolled_count": enrolled,
        "recent_grades": recent_grades,
        "recent_announcements": recent_ann,
    }

def instructor_dashboard():
    return {
        "students_count": User.query.filter_by(role="student").count(),
        "courses_count": Course.query.count(),
        "grades_count": Grade.query.count(),
        "announcements_count": Announcement.query.count(),
    }
