from ..models import Course, Announcement

def search_courses(q: str):
    q = (q or "").strip()
    if not q:
        return []
    return Course.query.filter((Course.code.contains(q)) | (Course.title.contains(q))).all()

def search_announcements(q: str):
    q = (q or "").strip()
    if not q:
        return []
    return Announcement.query.filter((Announcement.title.contains(q)) | (Announcement.body.contains(q))).all()
