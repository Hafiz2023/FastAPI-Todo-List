# This code defines a SQLAlchemy model class named 
# Todo representing a table in the database.
# The table is named "adil" (__tablename__).
# It has three columns: id as the primary key, name of type 
# String with indexing, and description of type String with indexing. 
# This model can be used to interact with the specified table in the database,
# providing a structured representation for TODO items with an associated
# name and description. The Base class from the database module is used as 
# the declarative base for this model.




from sqlalchemy import Column, Integer, String
from database import Base


class Todo(Base):
    __tablename__ = "adil"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
