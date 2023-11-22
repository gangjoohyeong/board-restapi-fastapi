from datetime import datetime
from pydantic import BaseModel, validator


class NoticeBase(BaseModel):
    id: int
    title: str
    content: str
    create_date: datetime
    
    class Config:
        orm_mode = True
        
class NoticeCreate(BaseModel):
    title: str
    content: str