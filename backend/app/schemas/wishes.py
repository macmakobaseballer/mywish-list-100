from typing import List
from pydantic import BaseModel


class Wish(BaseModel):
    wish_id: int
    account_id: str
    title: str
    description: str
    status: str

class WishList(BaseModel):
    account_id: str
    wishes: List[Wish]