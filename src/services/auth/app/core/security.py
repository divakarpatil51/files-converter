from passlib.context import CryptContext
from typing import Union, Any
from datetime import datetime, timedelta
import jwt

password_context = CryptContext(schemes=["bcrypt"])
ALGORITHM = "HS256"
KEY = "secret"


def create_access_token(subject: Union[str, Any]) -> str:
    expiry = datetime.utcnow() + timedelta(minutes=60)
    payload = {"exp": expiry, "sub": subject}

    return jwt.encode(payload=payload, key=KEY, algorithm=ALGORITHM)


def verify_password(password: str, hashed_password: str) -> bool:
    return password_context.verify(password, hashed_password)


def hash_password(password: str) -> str:
    return password_context.hash(password)
