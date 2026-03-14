from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie

from app.core.config import settings
from app.models.user_model import User


async def init_db():

    client = AsyncIOMotorClient(settings.mongodb_url)

    await init_beanie(
        database=client[settings.database_name],
        document_models=[User],
    )