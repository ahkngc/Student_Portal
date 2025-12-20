from __future__ import annotations

from flask import jsonify,request


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
    def success(data=None, status=200):
    return jsonify({
        "success": True,
        "data": data
    }), status


def failure(message, status=400):
    return jsonify({
        "success": False,
        "error": message
    }), status


def get_pagination():
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 10, type=int)

    if page < 1 or per_page < 1:
        return None

    return page, per_page


def paginate(query):
    pagination = get_pagination()
    if pagination is None:
        return None, failure("Invalid pagination parameters", 400)

    page, per_page = pagination
    result = query.paginate(page=page, per_page=per_page, error_out=False)

    return {
        "items": result.items,
        "page": page,
        "per_page": per_page,
        "total": result.total
    }, None
