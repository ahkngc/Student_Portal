from flask import Flask
from .config import Config
from .cli import register_cli
from .extensions import db, migrate
from . import models


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    @app.get("/health")
    def health():
        return {"status": "ok"}
    register_cli(app)

    return app
