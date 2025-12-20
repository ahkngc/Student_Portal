import click
from flask.cli import with_appcontext

from .extensions import db
from .models import Student, Course, Enrollment


def register_cli(app):
    @app.cli.command("seed")
    @with_appcontext
    def seed():
        """Seed the database with initial data."""

        courses_data = [
            {"title": "Python Programming", "code": "CS101"},
            {"title": "Databases", "code": "CS102"},
            {"title": "Web Development", "code": "CS103"},
        ]

        courses = []
        for data in courses_data:
            course = Course.query.filter_by(code=data["code"]).first()
            if not course:
                course = Course(title=data["title"], code=data["code"])
                db.session.add(course)
            courses.append(course)

        students_data = [
            {"name": "Ahmed Ali", "email": "ahmed@example.com"},
            {"name": "Sara Mohamed", "email": "sara@example.com"},
            {"name": "Omar Hassan", "email": "omar@example.com"},
        ]

        students = []
        for data in students_data:
            student = Student.query.filter_by(email=data["email"]).first()
            if not student:
                student = Student(name=data["name"], email=data["email"])
                db.session.add(student)
            students.append(student)

        db.session.commit()

        enrollments_data = [
            (students[0], courses[0]),
            (students[0], courses[1]),
            (students[1], courses[1]),
            (students[2], courses[2]),
        ]

        for student, course in enrollments_data:
            exists = Enrollment.query.filter_by(
                student_id=student.id,
                course_id=course.id
            ).first()

            if not exists:
                enrollment = Enrollment(
                    student_id=student.id,
                    course_id=course.id
                )
                db.session.add(enrollment)

        db.session.commit()

        click.echo("✅ Database seeded successfully.")
