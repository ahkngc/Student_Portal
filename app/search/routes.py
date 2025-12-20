from flask import Blueprint, render_template, request
from ..decorators import login_required
from ..auth.services import get_current_user
from .services import search_courses, search_announcements

bp = Blueprint("search", __name__, url_prefix="/search")

@bp.get("")
@login_required
def search_page():
    user = get_current_user()
    q = request.args.get("q", "")
    return render_template(
        "search.html",
        user=user,
        q=q,
        course_results=search_courses(q),
        announcement_results=search_announcements(q),
    )
