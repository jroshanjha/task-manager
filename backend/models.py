# 📦 backend/models.py
from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint, request, jsonify
import jwt, datetime
from functools import wraps
from flask import current_app as app

db = SQLAlchemy()

# drop database if exists taskdb;
#create database if not exists taskdb;

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(200))

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    user_id = db.Column(db.Integer)

task_bp = Blueprint('task', __name__)

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            user_id = data['user_id']
        except:
            return jsonify({"message": "Token is invalid!"}), 403
        return f(user_id, *args, **kwargs)
    return decorated

@task_bp.route('/tasks', methods=['GET'])
@token_required
def get_tasks(user_id):
    tasks = Task.query.filter_by(user_id=user_id).all()
    return jsonify([{"id": t.id, "title": t.title} for t in tasks])

@task_bp.route('/tasks', methods=['POST'])
@token_required
def add_task(user_id):
    data = request.get_json()
    task = Task(title=data['title'], user_id=user_id)
    db.session.add(task)
    db.session.commit()
    return jsonify({"message": "Task added"})

@task_bp.route('/tasks/<int:id>', methods=['DELETE'])
@token_required
def delete_task(user_id, id):
    Task.query.filter_by(id=id, user_id=user_id).delete()
    db.session.commit()
    return jsonify({"message": "Task deleted"})
