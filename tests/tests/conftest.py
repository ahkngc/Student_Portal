import pytest
from app import create_app, db as _db
from app.models import Student, Course, Enrollment, Grade

@pytest.fixture(scope='session')
def app():
    app = create_app(config_class='app.config.TestingConfig')
    with app.app_context():
        yield app

@pytest.fixture(scope='session')
def client(app):
    return app.test_client()

@pytest.fixture(scope='function')
def db_session(app):
    _db.create_all()
    yield _db.session
    _db.drop_all()

