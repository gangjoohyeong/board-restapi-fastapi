from sqlalchemy import Column, Integer, Text, String, DateTime
from database import Base


class Article(Base):
    __tablename__ = "articles"
    
    id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    title = Column(String(100), nullable=False)
    content = Column(Text, nullable=False)
    create_data = Column(DateTime, nullable=False)