from sqlalchemy.orm import Session
from models import Todo

def get_todos(db: Session):
    return db.query(Todo).all()

def create_todo(db: Session, title: str):
    todo = Todo(title=title)
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo

def update_todo(db: Session, todo_id: int, completed: bool):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if todo:
        todo.completed = completed
        db.commit()
    return todo

def delete_todo(db: Session, todo_id: int):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if todo:
        db.delete(todo)
        db.commit()
    return todo
