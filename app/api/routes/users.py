from fastapi import APIRouter

router = APIRouter(prefix="/user", tags=["users"])

@router.get("/",)
async def user():
    return {
        "id": 1,
        "name": "Max",
        "email": "max@gamil.com"
    }