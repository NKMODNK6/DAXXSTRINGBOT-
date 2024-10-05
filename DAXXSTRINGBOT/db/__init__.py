from motor.motor_asyncio import AsyncIOMotorClient
import config

_mongo_async_ = AsyncIOMotorClient(config.MONGO_DB_URI)
db = _mongo_async_.StringGen

