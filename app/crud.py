from sqlalchemy.orm import Session
from . import models, schemas

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_users(db: Session):
    return db.query(models.User).all()

def update_user(db: Session, user_id: int, user: schemas.UserCreate):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user:
        db_user.name = user.name
        db_user.email = user.email
        db.commit()
    return db_user

def delete_user(db: Session, user_id: int):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
    return user

# def create_task(db: Session, task: schemas.TaskCreate, user_id: int):
#     db_task = models.Task(title=task.title, user_id=user_id)
#     db.add(db_task)
#     db.commit()
#     db.refresh(db_task)
#     return db_task

# def get_task(db: Session, task_id: int):
#     return db.query(models.Task).filter(models.Task.id == task_id).first()

# def get_tasks(db: Session):
#     return db.query(models.Task).all()

# def update_task(db: Session, task_id: int, updated: schemas.TaskCreate):
#     task = get_task(db, task_id)
#     if task:
#         task.title = updated.title
#         db.commit()
#         db.refresh(task)
#     return task

# def delete_task(db: Session, task_id: int):
#     task = get_task(db, task_id)
#     if task:
#         db.delete(task)
#         db.commit()
#     return task

# def get_user_tasks(db: Session, user_id: int):
#     return db.query(models.Task).filter(models.Task.user_id == user_id).all()

# def get_user_task(db: Session, user_id: int, task_id: int):
#     return db.query(models.Task).filter(models.Task.user_id == user_id, models.Task.id == task_id).first()

# def update_user_task(db: Session, user_id: int, task_id: int, updated: schemas.TaskCreate):
#     task = get_user_task(db, user_id, task_id)
#     if task:
#         task.title = updated.title
#         db.commit()
#         db.refresh(task)
#     return task