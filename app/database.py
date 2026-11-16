
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncSession,
    async_sessionmaker
)

from sqlalchemy.orm import DeclarativeBase

from app.core.config import settings


# Create database engine
engine = create_async_engine(
    settings.DATABASE_URL,
    echo=True
)


# Create session factory
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)


# Base class for models
class Base(DeclarativeBase):
    pass


# Database session
async def get_db():

    async with AsyncSessionLocal() as session:
        yield session
