class Config:
    SECRET_KEY = "dev-secret-change-me"
    SQLALCHEMY_DATABASE_URI = "sqlite:///student_portal.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
