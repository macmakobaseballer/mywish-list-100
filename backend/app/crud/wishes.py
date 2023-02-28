from datetime import datetime
from logging import getLogger

from app.models.wishes import WishModel
from app.schemas.wishes import Wish



def create_wish_one(data: Wish):
    new_wish = WishModel(
        wish_id=data.wish_id,
        account_id=data.account_id,
        title=data.title,
        description=data.description,
    )
    new_wish.save()

    return {
        "status": 200,
        "message": "Created Successfully",
        "wish_id": new_wish.wish_id,
        "title": new_wish.title
    }

def get_wishes_all(account_id: str):
    all_wishes = WishModel.query(account_id)

    return {
        "wishes": all_wishes
    }