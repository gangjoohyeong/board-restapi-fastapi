from sqlalchemy import Column, Integer, Text, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

ArticleBase = declarative_base()


class Article(ArticleBase):
    __tablename__ = "articles"
    
    id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    title = Column(String(100), nullable=False)
    content = Column(Text, nullable=False)
    create_date = Column(DateTime, nullable=False)