from fastapi import APIRouter
from app.api.user_route import user_router
from app.api.login_route import login_router

api_router = APIRouter(prefix="/rest/v1")
api_router.include_router(user_router, prefix="/users", tags=["users"])
api_router.include_router(login_router, tags=["login"])
