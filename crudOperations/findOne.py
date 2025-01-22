from mongoDB import mongodb

async def findUser(email):
    user=await mongodb.collection.find_one({"email":email})
    print(user)
    return user
