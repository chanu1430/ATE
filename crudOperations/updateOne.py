from mongoDB import mongodb
from bson import ObjectId

async def updateUserStatus(objId:str, unique_id:str,new_status:str):
    obj_id=ObjectId(objId)
    result=await mongodb.collection.update_one(
        {"_id":obj_id,
         "token_details.token_id":unique_id},
        {"$set":{"token_details.$.status":new_status}}
    )
    return await updatedCount(result)






async def updateUserTokenId(objId:str,token_id:str):
    obj_id=ObjectId(objId)
    token_data={"token_id":token_id,"status":"Pending"}
    result= await mongodb.collection.update_one(
        {"_id":obj_id},
        {"$push":{"token_details":token_data}}
    )
    return await updatedCount(result)



async def updatedCount(result):
    if result.modified_count>0:
        print("updated the record")
        return True
    else:
        print("failed to upadate the record")
        return False