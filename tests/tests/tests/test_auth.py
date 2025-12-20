def test_protected_no_login(client):
    response = client.get("/admin-only")
    assert response.status_code == 401
