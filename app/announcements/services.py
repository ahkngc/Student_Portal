from ..extensions import db
from ..models import Announcement

def list_announcements():
    return Announcement.query.order_by(Announcement.created_at.desc()).all()

def create_announcement(title: str, body: str):
    a = Announcement(title=title.strip(), body=body.strip())
    db.session.add(a)
    db.session.commit()
    return a
