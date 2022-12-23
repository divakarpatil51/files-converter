import json
import logging

import requests
from app.core.config import settings
from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel

user_router = APIRouter()


class UserCreate(BaseModel):
    email: str
    password: str


logging.basicConfig(level=logging.INFO)


@user_router.post("")
def signup(*, user_request: UserCreate):
    resp = requests.post(
        f"{settings.AUTH_URL}/rest/v1/users",
        json=json.loads(user_request.json()),
        headers={"content-type": "application/json"},
    )

    if resp.status_code != 201:
        logging.exception(f"Error occurred while registering: {resp.text}")
        raise HTTPException(status_code=resp.status_code, detail=resp.text)
    return JSONResponse(status_code=201, content=resp.json())
