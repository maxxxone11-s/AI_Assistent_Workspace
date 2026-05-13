from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.schemas.user_schema import UserResponse
from app.services.user_service import get_user
from app.api.connect_db import get_db
from app.models.user_model import User

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/", response_model=UserResponse)
async def user(
    user_id: int,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(select(User).where(user_id == User.id))

    user = result.scalar_one_or_none()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user