from sqlalchemy.orm import Session
from models.notice import Notice
from schemas.notice import NoticeCreate
from datetime import datetime

def get_notice(db: Session, notice_id: int):
    db_notice = db.query(Notice).filter(Notice.id == notice_id).first()
    return db_notice

def get_notice_list(db: Session):
    notice_list = db.query(Notice).order_by(Notice.id.desc()).all()
    return notice_list

def create_notice(db: Session, notice_create: NoticeCreate):
    db_notice = Notice(title=notice_create.title,
                       content=notice_create.content,
                       create_date=datetime.now())
    
    db.add(db_notice)
    db.commit()
    return db_notice.id

def delete_notice(db: Session, db_notice: Notice):
    db.delete(db_notice)
    db.commit()
    return db_notice.id