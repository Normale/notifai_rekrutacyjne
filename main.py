from fastapi import FastAPI
import message
from database import init_models
import models
import asyncio


app = FastAPI()

app.include_router(
    message.router,
    prefix="/message",
)


@app.on_event("startup")
async def startup_event():
    await init_models()
