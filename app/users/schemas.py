from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class UserBaseSchema(BaseModel):
    name: str
    email: str

    class Config:
        orm_mode = True


class UserDetailSchema(UserBaseSchema):
    id: int
    created_at: datetime
    updated_at: Optional[datetime]


class UserCreateSchema(UserBaseSchema):
    password: str
