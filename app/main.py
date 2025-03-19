from fastapi import FastAPI
from app.db import models, engine
from app.api import notes

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(notes.router, prefix="/notes", tags=["notes"])
