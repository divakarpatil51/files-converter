from app.schemas.schemas import User, UserCreate
from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from app.api.deps import get_db
from app.repo.user_repo import user_repo

user_router = APIRouter()


@user_router.post("", response_model=User)
def create_user(*, db=Depends(get_db), user_request: UserCreate):
    user = user_repo.get_user_by_email(db, email=user_request.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail=f"User with emailL {user.email} already exists"
        )

    user = user_repo.create_user(db, user_request)
    user_resp = User(email=user.email)
    return user_resp
