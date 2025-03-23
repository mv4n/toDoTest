from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import crud, database

router = APIRouter()

@router.get("/todos")
def read_todos(db: Session = Depends(database.SessionLocal)):
    return crud.get_todos(db)

@router.post("/todos")
def add_todo(title: str, db: Session = Depends(database.SessionLocal)):
    return crud.create_todo(db, title)

@router.put("/todos/{todo_id}")
def toggle_todo(todo_id: int, completed: bool, db: Session = Depends(database.SessionLocal)):
    return crud.update_todo(db, todo_id, completed)

@router.delete("/todos/{todo_id}")
def remove_todo(todo_id: int, db: Session = Depends(database.SessionLocal)):
    return crud.delete_todo(db, todo_id)
