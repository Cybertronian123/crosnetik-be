from fastapi import FastAPI

from app.api.router import api_router

app = FastAPI(
    title="CrosNetik API",
    description="Backend API for CrosNetik",
    version="1.0.0",
)

app.include_router(api_router)
