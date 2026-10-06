from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.collection import Collection
from config.config import MONGODB_URI, DATABASE_NAME


class MongoDB:
    def __init__(self, uri: str, dbname: str):
        self.client = AsyncIOMotorClient(uri)
        self.db = self.client[dbname]

    def get_collection(self, name: str) -> Collection:
        return self.db[name]

mongodb = MongoDB(MONGODB_URI, DATABASE_NAME)
