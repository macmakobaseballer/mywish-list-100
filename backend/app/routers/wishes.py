from fastapi import APIRouter, Path
from app.crud.wishes import create_wish_one,get_wishes_all,get_wish_by_id

from app.schemas.wishes import Wish

router = APIRouter()


@router.get("/user/{login_id}/wishes")
async def get_wish_list(login_id: str):
    res = get_wishes_all(login_id)
    return res
    

@router.get("/user/{login_id}/wishes/{wish_id}")
async def get_wish(login_id: str,wish_id: int):
    res = get_wish_by_id(login_id,wish_id)
    return res

@router.post("/wishes")
async def create_wish_list(wish: Wish):
    res = create_wish_one(wish)
    return res

@router.put("/wishes/{wish_id}")
async def update_wish():
    pass


@router.delete("/wishes/{wish_id}")
async def delete_wish():
    pass
