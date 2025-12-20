from app import create_app

def test_login_page_loads():
    app = create_app()
    app.testing = True
    client = app.test_client()
    r = client.get("/login")
    assert r.status_code == 200
