import asyncio

from app.core.database import engine
from app.core.base import Base

DATABASE_URL = "postgresql+asyncpg://postgres:010SS@localhost:5432/ai_workspace"

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    