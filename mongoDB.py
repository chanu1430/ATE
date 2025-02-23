
from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

load_dotenv()

uri=os.getenv("MONGO_URI")
# Database and Collection Names
DATABASE_NAME = 'email_db'
COLLECTION_NAME = 'users'

# Initialize the MongoDB Client
class MongoDB:
    def __init__(self):
        self.client = AsyncIOMotorClient(uri)
        self.db = self.client[DATABASE_NAME]
        self.collection = self.db[COLLECTION_NAME]

    async def close_connection(self):
        self.client.close()


mongodb = MongoDB()
