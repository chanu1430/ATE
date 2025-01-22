from models import userModel
from mongoDB import mongodb

async def insertUser(userdata : userModel):
    userdict = userdata.dict()
    result = await mongodb.collection.insert_one(userdict)
    return result.inserted_id


