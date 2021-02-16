from datetime import datetime, timedelta
from typing import Optional

from db import get_db
from fastapi import APIRouter, Depends, HTTPException, status
from jose import jwt
from sqlalchemy.orm import Session
from users.models import UserModel
from utils.hashing import Hash
from utils.settings import JWT

from .schemas import LoginRequest, TokenResponse

router = APIRouter(prefix="/token", tags=["auth"])


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, JWT["SECRET_KEY"], algorithm=JWT["ALGORITHM"])
    return encoded_jwt


@router.post("/", response_model=TokenResponse)
def login(request: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.email == request.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials"
        )
    if not Hash.verify(user.password, request.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials"
        )

    access_token_expires = timedelta(minutes=JWT["ACCESS_TOKEN_EXPIRE_MINUTES"])
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
