from fastapi.responses import HTMLResponse
from crudOperations.updateOne import updateUserStatus

async def checkUserApproval(userData:dict,unique_id:str,status:str):
    try:
        checkUserToken=False
        checkUserTokenStatus=None
        objId=userData["_id"]
        if userData:
            user_token_details=userData["token_details"]
            for token in  user_token_details:
                if (token["token_id"]==unique_id):
                    checkUserToken=True
                    checkUserTokenStatus=token["status"]
                    break
            if checkUserToken:
                if checkUserTokenStatus=="Pending":
                    result =await updateUserStatus(objId,unique_id,status)
                    if result:
                        return HTMLResponse(f"<h1>Welcome User !</h1><p>Thank you for your response. {status}</p>")
                    else:
                        return HTMLResponse(f"<h1>Unable to update the token status</h1>")
                else:
                    return HTMLResponse(f"<h1>You Have Already Responded to this Request</h1>")
            else:
                return HTMLResponse(f"<h1>Sorry, This user token doesn't exists</h1>")
        else:
            return HTMLResponse(f"<h1>There is No user with this userId !</h1>")
    except Exception as e:
        return HTMLResponse(f"<h1>Error Occured {e}</h1>")