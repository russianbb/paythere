from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from utils.settings import DATABASE

SQLALCHEMY_URL = "mysql+pymysql://{user}:{password}@{host}/{name}".format(
    user=DATABASE["user"],
    password=DATABASE["password"],
    host=DATABASE["host"],
    name=DATABASE["name"],
)

engine = create_engine(SQLALCHEMY_URL, echo=True)
Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
