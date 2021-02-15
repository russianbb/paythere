from sqlalchemy import Column, Integer, String
from utils.db import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    fullname = Column(String(100))
    nickname = Column(String(50))

    def __repr__(self):
        return f"<User(name:{self.name}, fullname:{self.fullname}, nickname:{self.nickname}>"