from fastapi import FastAPI
from app.db.database import Base, _engine
from app.api.api import api_router

Base.metadata.create_all(bind=_engine)
app = FastAPI()
app.include_router(api_router)
