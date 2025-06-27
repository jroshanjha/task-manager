from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
# from app import models, schemas, crud
from app import models, schemas, crud
from app.database import SessionLocal, engine
import sys
import os
from fastapi.responses import RedirectResponse
from typing import List
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

#sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def get_db():
    db = SessionLocal()
    try: yield db
    finally: db.close()

@app.post("/users/", response_model=schemas.UserOut)
def create(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)

@app.get("/users/", response_model=List[schemas.UserOut])
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
    updated = crud.update_user(db, user_id, user)
    if not updated:
        raise HTTPException(status_code=404, detail="User not found")
    return updated

@app.delete("/users/{user_id}")
def delete(user_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_user(db, user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted"}

# @app.post("/login")
# async def login(username: str = Form(...), password: str = Form(...)):
#     # ✅ Replace with real authentication logic:
#     if username == "admin" and password == "secret":
#         # On successful login, redirect to /dashboard
#         return RedirectResponse(url="/dashboard", status_code=302)
#     else:
#         return {"error": "Invalid credentials"}

# @app.post("/login")
# async def login(username: str = Form(...), password: str = Form(...)):
#     if username == "admin" and password == "secret":
#         return RedirectResponse(url="https://www.google.com", status_code=302)
#     return {"error": "Invalid credentials"}
    
@app.post("/login/", response_model=schemas.UserLoginOut)
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    existing_user = crud.user_login(db, user)
    if not existing_user:
        raise HTTPException(status_code=404, detail="Invalid credentials")
    return existing_user

    # ✅ Redirect on successful login
    #return RedirectResponse(url=f"/users/{existing_user.id}", status_code=302)
    

@app.post("/register/", response_model=schemas.UserLoginOut)
def register(user: schemas.UserLogin, db: Session = Depends(get_db)):
    try:
        created_user = crud.user_register(db, user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    # if not created_user:
    #     raise HTTPException(status_code=400, detail="Registration failed")
    return created_user

    # crud.user_register(db,user)
    # On successful registration, redirect to /login
    #return RedirectResponse(url="/login", status_code=302)




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
