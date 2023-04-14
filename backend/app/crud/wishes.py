from datetime import datetime
from logging import getLogger

from app.models.wishes import WishModel
from app.schemas.wishes import Wish


def create_wish_one(item: Wish):
    new_wish = WishModel(
        wish_id=item.wish_id,
        login_id=item.login_id,
        title=item.title,
        description=item.description,
        status=item.status
    )
    new_wish.save()

    return {
        "message": "Created Successfully",
        "wish_id": new_wish.wish_id,
        "title": new_wish.title,
        "status": new_wish.status
    }

def get_wishes_all(login_id: str):
    wishes = WishModel.query(login_id)
    wish_list = []
    for wish in wishes:
        wish_list.append({
            "wish_id": wish.wish_id,
            "title": wish.title,
            "description": wish.description,
            "status": wish.status
        })

    return {
        "wishes": wish_list
    }

def get_wish_by_id(login_id: str, wish_id: int):
    a_wish = WishModel.get(login_id,wish_id)
    if a_wish:
        return {
            "wish_id": a_wish.wish_id,
            "title": a_wish.title,
            "description": a_wish.description,
            "status": a_wish.status
        }
    else:
        return {
            "status": 404,
            "message": "A wish not found"
        }