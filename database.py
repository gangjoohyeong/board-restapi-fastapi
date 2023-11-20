from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import yaml

with open('env.yaml', 'r') as yaml_conf:
    conf = yaml.safe_load(yaml_conf)

DB = conf['DATABASE']
db_user = DB['USER']
db_host = DB['HOST']
db_password = DB['PASSWORD']
db_port = DB['PORT']
db_database = DB['DB']

SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_database}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

# 데이터베이스 접속
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 데이터베이스 모델을 구성할 때 사용
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()