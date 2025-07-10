from dataEncryption import encrypt_data
from dataGeneration.generate_unique_id import generate_different_unique_id
from crudOperations.updateOne import updateUserTokenId
from bson import ObjectId
import aiofiles
import os

async def emailTemp(emailBody : str,obj_id:str):

    unique_id=await generate_different_unique_id(obj_id)

    await updateUserTokenId(obj_id,unique_id)
    objId=ObjectId(obj_id)


    result=f"{str(objId)}:{unique_id}"    #12324:12345678
    encToken=encrypt_data(result)

    template_path = os.path.join("public", "emailTemplate.html")

    async with aiofiles.open(template_path, mode="r", encoding="utf-8") as file:
        template_content = await file.read()

    return template_content.replace("{emailBody}", emailBody).replace("{encToken}", encToken)

