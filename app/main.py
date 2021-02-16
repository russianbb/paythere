from auth.views import router as auth_router
from db import engine
from fastapi import FastAPI
from users.views import router as users_router
from utils import models

models.Base.metadata.create_all(bind=engine)
app = FastAPI()


@app.get("/")
def ping():
    return {"ping": "pong"}


app.include_router(auth_router)
app.include_router(users_router)
