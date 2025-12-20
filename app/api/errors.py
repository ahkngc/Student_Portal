from __future__ import annotations

from flask import Flask
from werkzeug.exceptions import HTTPException

from .utils import error


def register_api_error_handlers(app: Flask):
    @app.errorhandler(404)
    def not_found(_e):
        return error("Not Found", 404)

    @app.errorhandler(405)
    def method_not_allowed(_e):
        return error("Method Not Allowed", 405)

    @app.errorhandler(400)
    def bad_request(_e):
        return error("Bad Request", 400)

    @app.errorhandler(500)
    def internal_error(_e):
        return error("Internal Server Error", 500)

    @app.errorhandler(HTTPException)
    def handle_http_exception(e: HTTPException):
        return error(e.description or "HTTP Error", e.code or 500)
