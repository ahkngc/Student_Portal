from .extensions import db


class Student(db.Model):
    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    enrollments = db.relationship("Enrollment", back_populates="student")

    def __repr__(self):
        return f"<Student {self.name}>"



class Course(db.Model):
    __tablename__ = "courses"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    code = db.Column(db.String(20), unique=True, nullable=False)

    enrollments = db.relationship("Enrollment", back_populates="course")

    def __repr__(self):
        return f"<Course {self.code}>"



class Enrollment(db.Model):
    __tablename__ = "enrollments"

    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey("students.id"))
    course_id = db.Column(db.Integer, db.ForeignKey("courses.id"))

    student = db.relationship("Student", back_populates="enrollments")
    course = db.relationship("Course", back_populates="enrollments")

    grade = db.relationship("Grade", uselist=False, back_populates="enrollment")



class Grade(db.Model):
    __tablename__ = "grades"

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(2), nullable=False)
    enrollment_id = db.Column(db.Integer, db.ForeignKey("enrollments.id"))
    enrollment = db.relationship("Enrollment", back_populates="grade")
    from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(50), nullable=False, default="student")

    def set_password(self, password: str):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)

