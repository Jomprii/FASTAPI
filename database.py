import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Using environment variable for database URL
database_url = os.environ.get("postgresql://fastapidb_216p_user:dr7GIIQskhleQ7qznHxm6WvnOrcOy2J7@dpg-cvvppkuuk2gs73difh50-a/fastapidb_216p")

# Creating the engine to interact with PostgreSQL
engine = create_engine(database_url, echo=True)

# Creating a session local class to interact with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class to create tables
Base = declarative_base()
