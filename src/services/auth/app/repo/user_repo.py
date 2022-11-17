from app.models.models import User
from app.schemas.schemas import UserCreate
from sqlalchemy.orm import Session
from app.core.security import hash_password, verify_password
from typing import Optional


class UserRepo:

    def create_user(self, db: Session, user_request: UserCreate) -> User:
        user = User(email=user_request.email, hashed_password=hash_password(user_request.password))
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    def get_user_by_email(self, db: Session, email: str) -> User:
        return db.query(User).filter(User.email == email).first()

    def authenticate(self, db: Session, email: str, password: str) -> Optional[User]:
        user = self.get_user_by_email(db, email=email)
        if not user or not verify_password(password=password, hashed_password=user.hashed_password):
            return None
        return user


user_repo = UserRepo()
