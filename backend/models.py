# backend/models.py

from pydantic import BaseModel

# Модель задачі
class Todo(BaseModel):
    text: str
    completed: bool = False
