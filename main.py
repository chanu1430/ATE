import os
from datetime import datetime,timedelta
from fastapi import FastAPI, HTTPException,Query
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from pydantic import EmailStr, BaseModel
from fastapi.responses import HTMLResponse
from typing import List
from emailTemplate import emailTemp
from dataEncryption import decrypt_data,encrypt_data
from models.userModel import userModel
from mongoDB import mongodb
from crudOperations.insertOne import insertUser
from crudOperations.findOne import findUserById,findUserByMail
from crudOperations.updateOne import updateUserStatus
from checkUserApproval import checkUserApproval
from dotenv import load_dotenv



app=FastAPI()
  
load_dotenv()

@app.get('/')
async def getApi():
    return {"msg":"Email Get Request"}


@app.get('/get-email/verify/approve/')
async def getEmail(token:str = Query(...)):
    try:
        objId,unique_id=decrypt_data(token).split(":")
        userData=await findUserById(objId)
        return await checkUserApproval(userData,unique_id,"Approve")
    except Exception as e:
        return HTTPException(status_code=500, detail=f"Invalid URL: {e}")
    

   

@app.get('/get-email/verify/decline/')
async def getEmail(token:str = Query(...)):
    try:
        objId,unique_id=decrypt_data(token).split(":")
        userData=await findUserById(objId)
        return await checkUserApproval(userData,unique_id,"Decline")
    except Exception as e:
        return HTTPException(status_code=500, detail=f"Failed to update Status: {e}")
    

   




conf = ConnectionConfig(
    MAIL_USERNAME=os.getenv("MAIL_USERNAME"),
    MAIL_PASSWORD=os.getenv("MAIL_PASSWORD"),
    MAIL_FROM=os.getenv("MAIL_FROM"),
    MAIL_PORT=int(os.getenv("MAIL_PORT",587)),
    MAIL_SERVER=os.getenv("MAIL_SERVER"),             
    MAIL_STARTTLS=True,                      
    MAIL_SSL_TLS=False,                       
    USE_CREDENTIALS=True    
)



class EmailModel(BaseModel):
    email: EmailStr
    subject: str
    body: str


@app.post("/send-email")
async def send_email(email: EmailModel):
   
    try:
        user_data=userModel(
             email=email.email,
             created_at=datetime.now(),
             expired_at=datetime.now() + timedelta(hours=1)

        )
        try:
            userExists=await findUserByMail(email.email)
            if userExists:
                print("user Already exists...................!")
                obj_id=userExists['_id']
               
            else:
                obj_id=await insertUser(user_data)
                print("New User Created......................!")
        except Exception as e:
            return {"message": f"Error Occurs while storing the data : {e}"}

        email_body=await emailTemp(email.body,str(obj_id))
        message = MessageSchema(
            subject=email.subject,
            recipients=[email.email],
            body= email_body,
            subtype="html"
        )
        fm = FastMail(conf)
        await fm.send_message(message)
        return {"message": "Email has been sent successfully"}
    except Exception as e: 
        raise HTTPException(status_code=500, detail=f"Failed to send email: {e}")
    





