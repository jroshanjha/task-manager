from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import SessionLocal, engine
import sys
import os
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def get_db():
    db = SessionLocal()
    try: yield db
    finally: db.close()

@app.post("/users/", response_model=schemas.UserOut)
def create(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)

@app.get("/users/", response_model=list[schemas.UserOut])
def read_all(db: Session = Depends(get_db)):
    return crud.get_users(db)

@app.get("/users/{user_id}", response_model=schemas.UserOut)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.put("/users/{user_id}")
def update(user_id: int, user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.update_user(db, user_id, user)

@app.delete("/users/{user_id}")
def delete(user_id: int, db: Session = Depends(get_db)):
    return crud.delete_user(db, user_id)

# @app.post("/tasks/", response_model=schemas.TaskOut)
# def create_task(task: schemas.TaskCreate, user_id: int, db: Session = Depends(get_db)):
#     return crud.create_task(db, task, user_id)

# @app.get("/tasks/", response_model=list[schemas.TaskOut])
# def read_all_tasks(db: Session = Depends(get_db)):
#     return crud.get_tasks(db)

# @app.get("/tasks/{task_id}", response_model=schemas.TaskOut)
# def read_task(task_id: int, db: Session = Depends(get_db)):
#     task = crud.get_task(db, task_id)
#     if not task:
#         raise HTTPException(status_code=404, detail="Task not found")
#     return task

# @app.put("/tasks/{task_id}")
# def update_task(task_id: int, task: schemas.TaskCreate, db: Session = Depends(get_db)):
#     return crud.update_task(db, task_id, task)

# @app.delete("/tasks/{task_id}")
# def delete_task(task_id: int, db: Session = Depends(get_db)):
#     return crud.delete_task(db, task_id)

# @app.get("/users/{user_id}/tasks/", response_model=list[schemas.TaskOut])
# def read_user_tasks(user_id: int, db: Session = Depends(get_db)):
#     return crud.get_user_tasks(db, user_id)

# @app.get("/users/{user_id}/tasks/{task_id}", response_model=schemas.TaskOut)
# def read_user_task(user_id: int, task_id: int, db: Session = Depends(get_db)):
#     return crud.get_user_task(db, user_id, task_id)

# @app.put("/users/{user_id}/tasks/{task_id}")
# def update_user_task(user_id: int, task_id: int, task: schemas.TaskCreate, db: Session = Depends(get_db)):
#     return crud.update_user_task(db, user_id, task_id, task)

# @app.delete("/users/{user_id}/tasks/{task_id}")
# def delete_user_task(user_id: int, task_id: int, db: Session = Depends(get_db)):
#     return crud.delete_user_task(db, user_id, task_id)
