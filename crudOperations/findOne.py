from mongoDB import mongodb
from bson import ObjectId

async def findUserByMail(email):
    user=await mongodb.collection.find_one({"email":email})
    print(user)
    return user

async def findUserById(objId):
    obj_id=ObjectId(objId)
    user=await mongodb.collection.find_one({"_id":obj_id})
    print(user)
    return user

async def findUserStatus(objId,uniqueId):
    obj_id=ObjectId(objId)
    user=await mongodb.collection.find_one({"_id":obj_id})
    

