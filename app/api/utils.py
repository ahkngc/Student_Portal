from __future__ import annotations

from flask import request


def ok(data=None, status_code: int = 200):
    payload = {"ok": True}
    if data is not None:
        payload["data"] = data
    return payload, status_code


def error(message: str, status_code: int = 400, details=None):
    payload = {"ok": False, "error": {"message": message}}
    if details is not None:
        payload["error"]["details"] = details
    return payload, status_code


def get_json_or_error(required: bool = True):
    """
    Returns parsed JSON dict or (error_payload, status_code) tuple.
    """
    if not request.is_json:
        if required:
            return error("Request must be JSON", 415)
        return {}
    data = request.get_json(silent=True)
    if data is None:
        return error("Invalid JSON body", 400)
    if not isinstance(data, dict):
        return error("JSON body must be an object", 400)
    return data
