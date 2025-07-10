from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from crudOperations.updateOne import updateUserStatus,updateUserStatusAndComments
from fastapi import Request

templates = Jinja2Templates(directory="public")

async def checkUserApproval(request:Request,userData:dict,unique_id:str,status:str,urlToken:str=None):
    try:
        # print("----------------token:"+token+"--------------------")
        checkUserToken=False
        checkUserTokenStatus=None
        objId=userData["_id"]
        if userData:
            user_token_details=userData["token_details"]
            for eachToken in  user_token_details:
                if (eachToken["token_id"]==unique_id):
                    checkUserToken=True
                    checkUserTokenStatus=eachToken["status"]
                    break
            if checkUserToken:
                if checkUserTokenStatus=="Pending":
                    if status=="Approve":
                        result =await updateUserStatus(objId,unique_id,status)
                        # print("--------------------------------")
                        # print(result)
                        # print("--------------------------------")
                        if result:
                            return HTMLResponse(f"<h1>Welcome User !</h1><p>Thank you for your response. {status}</p>")
                        else:
                            return HTMLResponse(f"<h1>Unable to update the token status</h1>")
                    else:
                        if urlToken is not None:
                            return templates.TemplateResponse("rejectTemplate.html", {
                                "request": request,
                                "message": f"Thank you for your response.",
                                "token":urlToken
                                })
                        else:
                            return HTMLResponse(f"<h1>Request must have valid token</h1>")
                else:
                    return HTMLResponse(f"<h1>You Have Already Responded to this Request</h1>")
            else:
                return HTMLResponse(f"<h1>Sorry, This user token doesn't exists</h1>")
        else:
            return HTMLResponse(f"<h1>There is No user with this userId !</h1>")
    except Exception as e:
        return HTMLResponse(f"<h1>Error Occured {e}</h1>")