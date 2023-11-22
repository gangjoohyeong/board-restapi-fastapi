from models.article import ArticleBase
from models.notice import NoticeBase

alembic_meta_data = [
    ArticleBase.metadata,
    NoticeBase.metadata,
]