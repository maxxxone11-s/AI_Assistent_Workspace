from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

engine = create_async_engine("подключение к db")

AsyncSessionLocal = async_sessionmaker(
    bing=engine,
    expire_on_commit=False
)

