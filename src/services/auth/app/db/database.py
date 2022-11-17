from sqlalchemy import engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings

_engine = engine.create_engine(settings.SQLALCHEMY_DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=_engine)
Base = declarative_base()
