from datetime import datetime
from logging import getLogger

from app.models.wishes import WishModel
from app.schemas.wishes import Wish


def create_wish_one(item: Wish):
    new_wish = WishModel(
        wish_id=item.wish_id,
        account_id=item.account_id,
        title=item.title,
        description=item.description,
    )
    new_wish.save()

    return {
        "status": 200,
        "message": "Created Successfully",
        "wish_id": new_wish.wish_id,
        "title": new_wish.title
    }

def get_wishes_all(account_id: str):
    wishes = WishModel.query(account_id)
    wish_list = []
    for wish in wishes:
        wish_list.append({
            "wish_id": wish.wish_id,
            "title": wish.title,
            "description": wish.description
        })

    return {
        "wishes": wish_list
    }
