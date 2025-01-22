
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
from crudOperations.findOne import findUser
from crudOperations.updateOne import updateUserStatus


app=FastAPI()
  

@app.get('/')
async def getApi():
    return {"msg":"Email Get Request"}


@app.get('/get-email/verify/approve/')
async def getEmail(token:str = Query(...)):
    try:
        objId,unique_id=decrypt_data(token).split(":")
        result =await updateUserStatus(objId,unique_id,"Approve")

        if result:
            return HTMLResponse(f"<h1>Welcome,{objId} !</h1><p>Thank you for your approve response.</p>")
        else:
            return HTMLResponse(f"<h1>Error,{objId} !</h1><p>Occured</p>")
    except Exception as e:
        return HTTPException(status_code=500, detail=f"Failed to update Status: {e}")
    

   

@app.get('/get-email/verify/decline/')
async def getEmail(token:str = Query(...)):
    try:
        objId,unique_id=decrypt_data(token).split(":")
        result =await updateUserStatus(objId,unique_id,"Decline")
        if result:
            return HTMLResponse(f"<h1>Welcome,{objId} !</h1><p>Thank you for your decline response.</p>")
        else:
            return HTMLResponse(f"<h1>Error,{objId} !</h1><p>Occured</p>")
    except Exception as e:
        return HTTPException(status_code=500, detail=f"Failed to update Status: {e}")
    

   




conf = ConnectionConfig(
    MAIL_USERNAME="chanakyanexus143@gmail.com",
    MAIL_PASSWORD="jwjm eers cmjq cknw",
    MAIL_FROM="chanakyanexus143@gmail.com",
    MAIL_PORT=587,
    MAIL_SERVER="smtp.gmail.com",             # Gmail SMTP server
    MAIL_STARTTLS=True,                       # Enable STARTTLS encryption
    MAIL_SSL_TLS=False,                       # Disable SSL/TLS encryption
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
            userExists=await findUser(email.email)
            if userExists:
                print("user Already exists...................!")
                obj_id=userExists['_id']
               
            else:
               
                obj_id=await insertUser(user_data)
                print("New User Created......................!")
        except Exception as e:
            return {"message": f"Error Occurs while storing the data : {e}"}
        
        print(str(obj_id))
        email_body=await emailTemp(email.body,str(obj_id))
        print("after email_body")
        message = MessageSchema(
            subject=email.subject,
            recipients=[email.email],
            body= email_body,
            subtype="html"
        )
        print(".........................................//////")
        fm = FastMail(conf)
        await fm.send_message(message)
        return {"message": "Email has been sent successfully"}
    except Exception as e: 
        raise HTTPException(status_code=500, detail=f"Failed to send email: {e}")
    





