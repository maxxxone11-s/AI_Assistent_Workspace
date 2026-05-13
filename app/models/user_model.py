from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.core.base import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    name: Mapped[str] = mapped_column(
        String(20),
        unique=False,
        nullable=False
    )

    email: Mapped[str] = mapped_column(
        unique=True,
        nullable=False
    )