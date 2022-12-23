import requests
from app.core.config import settings
from fastapi import APIRouter, Depends, logger
from fastapi.exceptions import HTTPException
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

login_router = APIRouter()


@login_router.post("/login")
def login(*, user_request: OAuth2PasswordRequestForm = Depends()):
    headers = {"content-type": "application/x-www-form-urlencoded"}
    req = {"username": user_request.username, "password": user_request.password}
    response = requests.post(
        f"{settings.AUTH_URL}/rest/v1/login", data=req, headers=headers
    )
    if response.status_code != 200:
        logger.logger.exception(f"Error: {response.reason}")
        raise HTTPException(status_code=401, detail="Unauthorized")
    return response.json()
