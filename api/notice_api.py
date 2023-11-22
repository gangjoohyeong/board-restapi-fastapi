from fastapi import APIRouter, Depends, HTTPException, status
from database import get_db
from schemas.notice import NoticeBase, NoticeCreate
from crud.notice_crud import get_notice, get_notice_list, create_notice, delete_notice
from typing import List
from sqlalchemy.orm import Session


router = APIRouter(
    prefix="/api/notices",
)

tags = ["notices"]

@router.get("/{notice_id}", response_model=NoticeBase, tags=tags)
def notice(notice_id: int, db: Session = Depends(get_db)):
    _notice = get_notice(db, notice_id)
    if _notice is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Notice not found")
    return _notice

@router.get("/", response_model=List[NoticeBase], tags=tags)
def notice_list(db: Session = Depends(get_db)):
    _notice_list = get_notice_list(db)
    return _notice_list

@router.post("/", tags=tags)
def notice_create(_notice_create: NoticeCreate, db: Session = Depends(get_db)):
    create_notice_id = create_notice(db, _notice_create)
    return {"create notice id": create_notice_id}

@router.delete("/{notice_id}", tags=tags)
def notice_delete(notice_id: int, db: Session = Depends(get_db)):
    _notice = get_notice(db, notice_id)
    if _notice is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Notice not found")
    delete_notice_id = delete_notice(db, _notice)
    return {"delete notice id": delete_notice_id}