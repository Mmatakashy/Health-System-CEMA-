from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SQLALCHEMY_DATABASE_URL = "sqlite:///./cema.db"  # or use PostgreSQL

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# PostgreSQL setup
SQLALCHEMY_DATABASE_URL = "postgresql://mmatam:yourpassword@localhost/cema_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# PostgreSQL setup
SQLALCHEMY_DATABASE_URL = "postgresql://username:password@localhost/cema_db"  # Replace with your actual credentials

# Create engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create session local
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create base class for models
Base = declarative_base()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
