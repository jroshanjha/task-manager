# === backend/tasks.py ===
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Task

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/tasks")
def get_tasks(db: Session = Depends(get_db)):
    return db.query(Task).all()

@router.post("/tasks")
def create_task(title: str, db: Session = Depends(get_db)):
    task = Task(title=title)
    db.add(task)
    db.commit()
    return task

@router.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    db.query(Task).filter(Task.id == task_id).delete()
    db.commit()
    return {"message": "Deleted"}

# === frontend/.env ===
# REACT_APP_API_URL=http://localhost:8000