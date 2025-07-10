from fastapi import Request,HTTPException,APIRouter,Form
from dataEncryption import decrypt_data
from crudOperations.findOne import findUserById
from crudOperations.updateOne import updateUserStatusAndComments

router = APIRouter()

@router.post("/")
async def rejectCommentsHandler(comments:str=Form(...),token:str=Form(...)):
    try:
        objId,unique_id=decrypt_data(token).split(":")
        await findUserById(objId)
        updateStatus=await updateUserStatusAndComments(objId,unique_id,"Reject",comments)
        if(updateStatus):
            return {"status":"success","msg":"Successfully updated the status"}
        else:
            return {"status":"fail","msg":"Failed to update the status"}
    except Exception as e:
        return HTTPException(status_code=500, detail=f"Invalid URL: {e}")



