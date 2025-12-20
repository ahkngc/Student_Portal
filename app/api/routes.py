from . import api_bp
from .utils import success, failure, paginate


@api_bp.get("/students")
def get_students():
    data, error = paginate(Student.query)
    if error:
        return error

    return success({
        "items": [s.to_dict() for s in data["items"]],
        "page": data["page"],
        "per_page": data["per_page"],
        "total": data["total"]
    })


@api_bp.get("/ping")
def ping():
    return {"message": "pong"}
