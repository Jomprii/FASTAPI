import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Get the database URL from the environment variable
database_url = os.environ.get("FastAPIDB")

if not database_url:
    raise ValueError("No DATABASE_URL found in environment variables.")

# Create the engine to interact with PostgreSQL
engine = create_engine(database_url, echo=True)

# Create a session local class to interact with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class to create tables
Base = declarative_base()
