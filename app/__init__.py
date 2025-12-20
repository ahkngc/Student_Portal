from flask import Flask
from .config import Config
from .cli import register_cli
from .api import api_bp
from .api.errors import register_api_error_handlers
from .extensions import db, migrate
from . import models


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    register_api_error_handlers(app)
    app.register_blueprint(api_bp, url_prefix="/api/v1")


    @app.get("/health")
    def health():
        return {"status": "ok"}
    register_cli(app)

    return app
