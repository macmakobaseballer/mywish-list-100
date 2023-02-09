from typing import List
from pydantic import BaseModel


class Wish(BaseModel):
    id: int
    title: str
    memo: str
    status: str

class WishList(BaseModel):
    wishes: List[Wish]