from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from src.config import settings

DB_URI = settings.DB_URI

engine = create_engine(DB_URI)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db() -> SessionLocal:
    db = SessionLocal()
    try:
        return db
    finally:
        db.close()
