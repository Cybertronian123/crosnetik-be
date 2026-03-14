from fastapi import FastAPI
from app.db.init_db import init_db
from app.api.router import api_router

app = FastAPI(
    title="CrosNetik API",
    description="Backend API for CrosNetik",
    version="1.0.0",
)

app.include_router(api_router)


@app.on_event("startup")
async def start_database():
    await init_db()
