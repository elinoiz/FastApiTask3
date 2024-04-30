import asyncio
import pytest
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Actor, Movie
from sqlalchemy import select


DATABASE_URL = 'postgresql+asyncpg://postgres:1234@localhost:5432/movie'

async_engine = create_async_engine(DATABASE_URL, echo=True)
async_session = sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)

@pytest.fixture(scope="session")
def event_loop():
    yield asyncio.get_event_loop()

@pytest.fixture(scope="session")
async def async_engine():
    async_engine = create_async_engine(DATABASE_URL, echo=True)
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield async_engine
    async_engine.dispose()

@pytest.fixture(scope="session")
def async_session(event_loop, async_engine):
    async_session = sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)
    yield async_session()
    event_loop.run_until_complete(async_session.close())

@pytest.fixture(scope="session")
async def async_db(async_engine):
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    async_session = sessionmaker(async_engine, class_=AsyncSession)
    async with async_session() as session:
        yield session

async def test_actors_table_created(async_db):
    # Проверяем, что таблица актеров была успешно создана
    async with async_db() as session:
        assert await session.execute(select(Actor).count()) == 0

async def test_movies_table_created(async_db):
    # Проверяем, что таблица фильмов была успешно создана
    async with async_db() as session:
        assert await session.execute(select(Movie).count()) == 0
