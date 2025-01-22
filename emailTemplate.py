from dataEncryption import encrypt_data
from dataGeneration.generate_unique_id import generate_different_unique_id
from crudOperations.updateOne import updateUserTokenId
from bson import ObjectId

async def emailTemp(emailBody : str,obj_id:str):

    unique_id=await generate_different_unique_id(obj_id)
    await updateUserTokenId(obj_id,unique_id)
    objId=ObjectId(obj_id)
    result=f"{str(objId)}:{unique_id}"
    encToken=encrypt_data(result)

    button_html =f"""
        <html>
            <body >
                
                <h2>Email Approval</h2>
                <p>{emailBody}</p>
                <div style="border:2px solid black; border-radius:4px; padding:20px 20px">
                  
                    <center>
                         <h4>Please Complete This Approval</h4>
                         <a href="http://127.0.0.1:8000/get-email/verify/approve?token={encToken}" style="background-color: #4CAF50; color: white; padding: 10px 20px;margin:10px ; text-align: center; text-decoration: none; display: inline-block; font-size: 16px; border-radius: 4px;">Approve</a>
                         <a href="http://127.0.0.1:8000/get-email/verify/decline?token={encToken}" style="background-color: #e05858; color: white; padding: 10px 20px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px; border-radius: 4px;">Reject</a>
                
                    </center>
                   
                </div>
               
                
            </body>
        </html>
    """
    return button_html