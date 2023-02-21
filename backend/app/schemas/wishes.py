from typing import List
from pydantic import BaseModel


class Wish(BaseModel):
    wish_id: int
    title: str
    memo: str
    status: str

class WishList(BaseModel):
    account_id: str
    wishes: List[Wish]