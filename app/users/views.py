from typing import List

from db import get_db
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from utils.hashing import Hash

from .models import UserModel
from .schemas import UserCreateSchema, UserDetailSchema

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/", response_model=List[UserDetailSchema])
def list(db: Session = Depends(get_db)):
    users = db.query(UserModel).all()
    return users


@router.post("/", response_model=UserDetailSchema, status_code=201)
def create(request: UserCreateSchema, db: Session = Depends(get_db)):
    new_user = UserModel(**request.dict())
    new_user.password = Hash.bcrypt(new_user.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
