from app import create_app

def test_courses_requires_login():
    app = create_app()
    app.testing = True
    client = app.test_client()
    r = client.get("/courses", follow_redirects=False)
    assert r.status_code in (301, 302)
