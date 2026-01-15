from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.api.router import api_router
from app.core.database import create_tables

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    await create_tables()
    yield
    # Shutdown

app = FastAPI(title="Contract First API", version="1.0.0", lifespan=lifespan)

app.include_router(api_router)