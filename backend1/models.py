# === backend/models.py ===
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from database import Base   

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    is_admin = Column(Boolean, default=False)

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey("users.id"))
