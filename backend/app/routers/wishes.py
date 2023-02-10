from fastapi import APIRouter

router = APIRouter()


@router.get("/wishes")
async def get_wish_list():
    pass

@router.get("/wishes/{id}")
async def get_wish_by_id():
    pass

@router.post("/wishes")
async def create_wish_list():
    pass

@router.put("/wishes/{id}")
async def update_wish():
    pass


@router.delete("/wishes/{id}")
async def delete_wish():
    pass
