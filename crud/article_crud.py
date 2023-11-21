from sqlalchemy.orm import Session
from models.article import Article
from schemas.article import ArticleCreate
from datetime import datetime

def get_article_list(db: Session):
    article_list = db.query(Article).order_by(Article.create_date.desc()).all()
    return article_list

def create_article(db: Session, article_create: ArticleCreate):
    db_article = Article(title=article_create.title, 
                         content=article_create.content, 
                         create_date=datetime.now())
    
    db.add(db_article)
    db.commit()
    return db_article.id