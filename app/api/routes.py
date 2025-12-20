from . import api_bp


@api_bp.get("/ping")
def ping():
    return {"message": "pong"}
