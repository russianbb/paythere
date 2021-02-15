from sqlalchemy import Column, Integer, Unicode

from utils.models import BaseModel


class User(BaseModel):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(Unicode(64), nullable=False)
    email = Column(Unicode(64), nullable=False)
