# 🔐 backend/auth.py — JWT Auth Logic
from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import jwt, datetime
from models import db, User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    hashed = generate_password_hash(data['password'])
    user = User(username=data['username'], password=hashed)
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "Registered successfully"}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if user and check_password_hash(user.password, data['password']):
        token = jwt.encode({
            'user_id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }, 'supersecret', algorithm='HS256')
        return jsonify({"token": token})
    return jsonify({"message": "Invalid credentials"}), 401
