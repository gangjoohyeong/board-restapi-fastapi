from fastapi import APIRouter, Depends, HTTPException, status
from database import get_db
from schemas.article import ArticleBase, ArticleCreate
from crud.article_crud import get_article, get_article_list, create_article
from typing import List
from sqlalchemy.orm import Session


router = APIRouter(
    prefix="/api/articles",
)

tags = ["articles"]

@router.get("/{article_id}", response_model=ArticleBase, tags=tags)
def article(article_id: int, db: Session = Depends(get_db)):
    _article = get_article(db, article_id)
    if _article is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Article not found")
    return _article

@router.get("/", response_model=List[ArticleBase], tags=tags)
def article_list(db: Session = Depends(get_db)):
    _artlcle_list = get_article_list(db)
    return _artlcle_list

@router.post("/", tags=tags)
def article_create(_article_create: ArticleCreate, db: Session = Depends(get_db)):
    create_article_id = create_article(db, _article_create)
    return {"create article id": create_article_id}
