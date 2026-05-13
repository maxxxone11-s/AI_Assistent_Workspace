from sqlalchemy import create_engine, MetaData, Table

from app.core.database import engine

metadata = MetaData()

metadata.create_all(engine)