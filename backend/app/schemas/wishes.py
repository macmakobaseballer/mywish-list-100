from typing import List
from pydantic import BaseModel


class Wish(BaseModel):
    wish_id: int
    login_id: str
    title: str
    description: str
    status: str

class WishList(BaseModel):
    login_id: str
    wishes: List[Wish]