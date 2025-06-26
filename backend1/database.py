# ✅ Backend using FastAPI + MySQL

# === backend/database.py ===
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

from dotenv import load_dotenv
load_dotenv()

# MySQL connection string (edit values as needed or use environment variables)
password = 'jroshan%4098'
DATABASE_URL = os.getenv("DATABASE_URL", f"mysql+pymysql://root:{password}@localhost:3306/taskdb")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()
