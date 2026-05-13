from fastapi import APIRouter

from app.schemas.user_schema import UserResponse
from app.services.user_service import get_user

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/", response_model=UserResponse)
async def user():
    return get_user()