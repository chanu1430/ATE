from datetime import datetime
from typing import List
from pydantic import BaseModel,EmailStr,validator


class tokenData(BaseModel):
    token_id:str
    status:str

class userModel(BaseModel):
    email:EmailStr
    clicked:bool = False
    created_at:datetime
    expired_at:datetime
    token_details:List[tokenData] = []



    @validator('created_at', pre=True)
    def format_created_at(cls, v: datetime) -> str:
        return v.isoformat()
    
    @validator('expired_at', pre=True)
    def format_expired_at(cls, v: datetime) -> str:
        return v.isoformat()
    






