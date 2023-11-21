from datetime import datetime
from pydantic import BaseModel, validator


class ArticleBase(BaseModel):
    id: int
    title: str
    content: str
    create_date: datetime
    
    class Config:
        orm_mode = True
        
class ArticleCreate(BaseModel):
    title: str
    content: str