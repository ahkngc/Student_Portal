from flask import Flask
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    @app.get("/health")
    def health():
        return {"status": "ok"}

    return app
