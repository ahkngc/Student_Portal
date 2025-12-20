from .extensions import db
from .models import User, Course, Enrollment, Grade, Announcement

def seed_demo_data():
    if User.query.first():
        return

    instructor = User(name="Dr Instructor", email="instructor@demo.com", role="instructor")
    instructor.set_password("1234")

    s1 = User(name="Ahmed Student", email="student1@demo.com", role="student"); s1.set_password("1234")
    s2 = User(name="Mona Student", email="student2@demo.com", role="student"); s2.set_password("1234")

    db.session.add_all([instructor, s1, s2])
    db.session.flush()

    c1 = Course(code="CS101", title="Intro to Programming")
    c2 = Course(code="SE201", title="Software Engineering")
    db.session.add_all([c1, c2])
    db.session.flush()

    db.session.add_all([
        Enrollment(user_id=s1.id, course_id=c1.id),
        Enrollment(user_id=s1.id, course_id=c2.id),
        Enrollment(user_id=s2.id, course_id=c1.id),
    ])

    db.session.add_all([
        Grade(user_id=s1.id, course_id=c1.id, item_name="Midterm", score=28),
        Grade(user_id=s1.id, course_id=c2.id, item_name="Quiz", score=15),
        Grade(user_id=s2.id, course_id=c1.id, item_name="Midterm", score=25),
    ])

    db.session.add(Announcement(title="Welcome", body="Welcome to the Student Portal!"))
    db.session.commit()
