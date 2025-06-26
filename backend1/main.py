# from fastapi import FastAPI, Depends, HTTPException
# from fastapi.middleware.cors import CORSMiddleware
# from sqlalchemy.orm import Session
# import models, schemas, crud
# from database import SessionLocal, engine, Base
# from fastapi.security import OAuth2PasswordBearer
# from fastapi import Depends
# from jwt_handler import decode_token
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
# # from dotenv import load_dotenv
# # load_dotenv()

# def get_current_user(token: str = Depends(oauth2_scheme)):
#     payload = decode_token(token)
#     return payload

# Base.metadata.create_all(bind=engine)

# app = FastAPI()

# # Allow React frontend
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:3000"],
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# @app.get("/tasks", response_model=list[schemas.Task])
# def read_tasks(db: Session = Depends(get_db)):
#     return crud.get_tasks(db)

# @app.post("/tasks", response_model=schemas.Task)
# def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
#     return crud.create_task(db, task)

# @app.put("/tasks/{task_id}", response_model=schemas.Task)
# def update_task(task_id: int, task: schemas.TaskCreate, db: Session = Depends(get_db)):
#     return crud.update_task(db, task_id, task)

# @app.delete("/tasks/{task_id}")
# def delete_task(task_id: int, db: Session = Depends(get_db)):
#     return crud.delete_task(db, task_id)


# === backend/main.py ===
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from users import router as user_router
from tasks import router as task_router
from database import Base, engine

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)
app.include_router(user_router)
app.include_router(task_router)