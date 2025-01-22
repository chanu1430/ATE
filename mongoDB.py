
from motor.motor_asyncio import AsyncIOMotorClient

uri="mongodb+srv://chanakyanexus143:gEoFYo78bWsIAMyR@emailapproval.u5sj3.mongodb.net/?retryWrites=true&w=majority&appName=EmailApproval"
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
