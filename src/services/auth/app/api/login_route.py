from fastapi import APIRouter, Depends
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from app.api.deps import get_db
from app.repo.user_repo import user_repo
from fastapi.exceptions import HTTPException
from app.core.security import create_access_token

login_router = APIRouter()


@login_router.post("/login")
def login(*, db=Depends(get_db), user_request: OAuth2PasswordRequestForm = Depends()):
    user = user_repo.authenticate(db, email=user_request.username, password=user_request.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    return {
        "access_token": create_access_token(user.email),
        "token_type": "bearer"
    }
