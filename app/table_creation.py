from sqlalchemy import create_engine, MetaData

from app.core.database import engine
from app.core.base import Base

metadata = MetaData()

Base.metadata.create_all(engine)