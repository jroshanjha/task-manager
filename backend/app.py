# 🖥️ Backend Setup (Flask + JWT)
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from auth import auth_bp
from models import db, task_bp
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI")  # ✅ critical line
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")

db.init_app(app)

app.register_blueprint(auth_bp)
app.register_blueprint(task_bp)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return "✅ Flask-MySQL is working"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

# # 🖥️ Backend Setup (FastAPI + JWT)
# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from auth import auth_bp
# from tasks import task_bp

# app = FastAPI()

# origins = ["*"]
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# app.include_router(auth_bp)
# app.include_router(task_bp)
