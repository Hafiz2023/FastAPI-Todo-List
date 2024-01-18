# main.py
# This FastAPI code defines an API with three endpoints for creating, 
# updating, and deleting TODO items. It uses SQLAlchemy for database operations,
# including model definition and session management. 
# The API supports POST to create a new TODO, PUT to update an existing one, 
# and DELETE to remove a TODO. Pydantic models (Todos and TodoUpdate)
# validate the input data. Database sessions are managed using a dependency 
# function (get_db). The code efficiently handles HTTPExceptions and ensures 
# proper interaction with the database.


from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
import models
from pydantic import BaseModel
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine) # create tables in database    

class Todos(BaseModel): # pydantic model for todo
    
    name: str
    description: str


class TodoUpdate(BaseModel): # pydantic model for todo update
    
    
    name: str
    description: str


app = FastAPI() #   FastAPI instance

# Dependency


def get_db(): # get database session
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# post method 
@app.post("/todos/")
def create_todo(todo: Todos, db: Session = Depends(get_db)):
    new_todo = models.Todo(name=todo.name,
                    description=todo.description)
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo

# put method
@app.put("/todos/{todo_id}") 
def update_todo(todo_id: int, updated_todo: TodoUpdate, db: Session = Depends(get_db)):
    db_todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    db_todo.name = updated_todo.name, # type: ignore
    db_todo.description = updated_todo.description # type: ignore
    db.commit()
    db.refresh(db_todo)
    return db_todo


# delete method
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    db_todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.delete(db_todo)
    db.commit()
    return {"message": "Todo deleted"}
