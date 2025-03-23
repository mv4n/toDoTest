from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, Integer, String, Boolean
from databases import Database

DATABASE_URL = "sqlite+aiosqlite:///./todos.db"

database = Database(DATABASE_URL)
engine = create_async_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
Base = declarative_base()

app = FastAPI()

# Модель Todo
class Todo(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, index=True)
    completed = Column(Boolean, default=False)

# Створення таблиць
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.on_event("startup")
async def startup():
    await database.connect()
    await init_db()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

# Отримати всі задачі
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}


@app.get("/todos/")
async def read_todos(session: AsyncSession = Depends(SessionLocal)):
    result = await session.execute("SELECT * FROM todos")
    return result.mappings().all()

# Додати нову задачу
@app.post("/todos/")
async def create_todo(todo: dict, session: AsyncSession = Depends(SessionLocal)):
    new_todo = Todo(text=todo["text"], completed=False)
    session.add(new_todo)
    await session.commit()
    await session.refresh(new_todo)
    return new_todo
