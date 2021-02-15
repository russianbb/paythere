from datetime import datetime

from sqlalchemy import Column, DateTime

from db import Base


class BaseModel(Base):
    __abstract__ = True

    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=True, onupdate=datetime.utcnow)
