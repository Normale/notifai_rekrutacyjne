from fastapi import FastAPI
import message
from database import engine
import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(
    message.router,
    prefix="/message",
)
