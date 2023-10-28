from sqlalchemy import create_engine;
from sqlalchemy.orm import sessionmaker, declarative_base

import settings 

# Crete database engine

engine = create_engine(settings.DATABASE_URL, echo=True, future=True)


# Create database declerative base

Base = declarative_base()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    """Database session generator"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()