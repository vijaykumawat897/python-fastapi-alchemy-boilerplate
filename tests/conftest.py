###### NOT REQUIRED IF MOCKING IS USED ######
###### UNCOMMENT WHEN USING REAL DB ######

# import asyncio
# import os
# from httpx import ASGITransport, AsyncClient
# import pytest
# from sqlalchemy.ext.asyncio import (
#     AsyncSession,
#     create_async_engine,
#     async_sessionmaker,
# )

# from app.models.base import Base
# from app.main import app
# from app.core.database import get_db
# from app.core.config import config

# DATABASE_URL = config.TEST_DATABASE_URL

# # -------------------------
# # Test engine
# # -------------------------
# @pytest.fixture
# async def engine():
#     engine = create_async_engine(
#         DATABASE_URL,
#         future=True,
#         echo=False,
#     )

#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)

#     yield engine

#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.drop_all)

#     await engine.dispose()


# # -------------------------
# # DB session per test
# # -------------------------
# @pytest.fixture
# async def db_session(engine) -> AsyncSession:
#     async_session = async_sessionmaker(engine, expire_on_commit=False)
#     async with async_session() as session:
#         yield session
#         # await session.rollback()


# # -------------------------
# # Override FastAPI dependency
# # -------------------------
# @pytest.fixture
# async def client(db_session):
#     async def override_get_db():
#         yield db_session

#     app.dependency_overrides[get_db] = override_get_db

#     transport = ASGITransport(app=app)

#     async with AsyncClient(
#         transport=transport,
#         base_url="http://test",
#     ) as client:
#         yield client

#     app.dependency_overrides.clear()