def test_invalid_grade(db_session, client):
    student = Student(name="S1")
    course = Course(title="C1")
    db_session.add_all([student, course])
    db_session.commit()

    data = {"student_id": student.id, "course_id": course.id, "grade": 101}
    response = client.post("/grades", json=data)
    assert response.status_code == 400
