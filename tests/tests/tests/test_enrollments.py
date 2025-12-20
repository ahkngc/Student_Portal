def test_enroll_student(db_session, client):
    student = Student(name="Test Student")
    course = Course(title="Test Course")
    db_session.add_all([student, course])
    db_session.commit()

    data = {"student_id": student.id, "course_id": course.id}
    response = client.post("/enroll", json=data)
    assert response.status_code == 201

def test_duplicate_enrollment(db_session, client):
    student = Student(name="Student 1")
    course = Course(title="Course 1")
    db_session.add_all([student, course])
    db_session.commit()

    data = {"student_id": student.id, "course_id": course.id}
    client.post("/enroll", json=data)
    response = client.post("/enroll", json=data)
    assert response.status_code in (400, 409)
