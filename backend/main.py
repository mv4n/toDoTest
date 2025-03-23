from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Додаємо CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # дозволяємо доступ з усіх джерел
    allow_credentials=True,
    allow_methods=["*"],  # дозволяємо всі методи (GET, POST, PUT, DELETE)
    allow_headers=["*"],  # дозволяємо всі заголовки
)

# Список задач в пам'яті
todos = []

# Модель для задачі
class Todo(BaseModel):
    id: int
    text: str
    completed: bool

@app.get("/todos/", response_model=List[Todo])
async def get_todos():
    return todos

@app.post("/todos/", response_model=Todo)
async def create_todo(todo: Todo):
    todos.append(todo)
    return todo
