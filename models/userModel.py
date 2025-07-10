from datetime import datetime
from typing import List,Optional
from pydantic import BaseModel,EmailStr,validator


class tokenData(BaseModel):
    token_id:str
    status:str
    comments: Optional[str] = None


class userModel(BaseModel):
    email:EmailStr
    created_at:datetime
    expired_at:datetime
    token_details:List[tokenData] = []



    @validator('created_at', pre=True)
    def format_created_at(cls, v: datetime) -> str:
        return v.isoformat()
    
    @validator('expired_at', pre=True)
    def format_expired_at(cls, v: datetime) -> str:
        return v.isoformat()
    






