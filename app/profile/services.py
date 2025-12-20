from ..extensions import db
from ..models import User

def get_profile(user_id: int):
    return User.query.get(user_id)

def change_password(user: User, new_password: str):
    user.set_password(new_password)
    db.session.commit()
