from flask import Flask
from .config import Config
from .cli import register_cli
from .api import api_bp
from .api.errors import register_api_error_handlers
from .extensions import db, migrate
from . import models
from .extensions import login_manager
from .models import User


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    register_api_error_handlers(app)
    app.register_blueprint(api_bp, url_prefix="/api/v1")
    
    login_manager.init_app(app)


    @app.get("/health")
    def health():
        return {"status": "ok"}
    register_cli(app)
    
    return app

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
