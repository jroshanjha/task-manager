# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
# from backend.auth import hash_password, verify_password
# from token import create_access_token
# from database import SessionLocal
# from models import User  # Add User model
# from schemas import UserCreate, UserLogin, Token

# router = APIRouter()

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# @router.post("/register")
# def register(user: UserCreate, db: Session = Depends(get_db)):
#     existing = db.query(User).filter(User.email == user.email).first()
#     if existing:
#         raise HTTPException(status_code=400, detail="Email already exists")
#     new_user = User(email=user.email, hashed_password=hash_password(user.password), is_admin=user.is_admin)
#     db.add(new_user)
#     db.commit()
#     return {"msg": "Registered successfully"}

# @router.post("/login", response_model=Token)
# def login(user: UserLogin, db: Session = Depends(get_db)):
#     db_user = db.query(User).filter(User.email == user.email).first()
#     if not db_user or not verify_password(user.password, db_user.hashed_password):
#         raise HTTPException(status_code=401, detail="Invalid credentials")
#     token = create_access_token({"sub": db_user.email, "is_admin": db_user.is_admin})
#     return {"access_token": token, "token_type": "bearer"}

# === backend/users.py ===
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import User
from passlib.hash import bcrypt
from jwt_handler import create_access_token

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register")
def register_user(email: str, password: str, db: Session = Depends(get_db)):
    if db.query(User).filter(User.email == email).first():
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = bcrypt.hash(password)
    user = User(email=email, hashed_password=hashed_password)
    db.add(user)
    db.commit()
    return {"message": "User registered"}

@router.post("/login")
def login_user(email: str, password: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == email).first()
    if not user or not bcrypt.verify(password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    access_token = create_access_token({"sub": user.email, "is_admin": user.is_admin})
    return {"access_token": access_token}