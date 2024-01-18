# database.py
# This Python code sets up a connection to a PostgreSQL 
# database using SQLAlchemy. It defines an engine for the connection,
# a session for managing interactions with the database, 
# and a base class for creating declarative models. The provided 
# PostgreSQL URL contains the necessary credentials and connection details.
# This foundation allows developers to define and interact with database models
# within their application.


from sqlalchemy import create_engine 
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import sessionmaker
SQLALCHEMY_DATABASE_URL = "postgresql://adilamin374:7SbiVTP2HIJN@ep-lucky-tooth-51281465-pooler.ap-southeast-1.aws.neon.tech/demo?sslmode=require"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db = SessionLocal()
Base = declarative_base()


