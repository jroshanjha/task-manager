# from fastapi import FastAPI, Request, HTTPException
# from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel,EmailStr, Field,validator,constr
# from fastapi.staticfiles import StaticFiles
# import mysql.connector
# from dotenv import load_dotenv
# import re
# app = FastAPI()

# # # Allow React frontend
# # app.add_middleware(
# #     CORSMiddleware,
# #     allow_origins=["http://localhost:3000"],
# #     allow_methods=["*"],
# #     allow_headers=["*"],
# # )

# # Mysql connect function
# conn = mysql.connector.connect(
#     host="localhost",
#     user ='root',
#     password='jroshan@98',
#     database='testdb'
# )

# cursor = conn.cursor(dictionary=True)
# # Load environment variables from .env file
# load_dotenv()

# # Pydantic Model
# class User(BaseModel):
#     name: constr(strip_whitespace=True, min_length=2, max_length=50)
#     email: EmailStr
    
#     @validator('name')
#     def validate_name(cls, v):
#         if not re.match("^[A-Za-z ]+$", v):
#             raise ValueError('Name must contain only letters and spaces')
#         return v
    
# @app.post("/users/")
# def create_user(user: User):
#     query = "INSERT INTO users (name, email) VALUES (%s, %s)"
#     cursor.execute(query, (user.name, user.email))
#     conn.commit()
#     return {"message": "User created", "id": cursor.lastrowid}

# @app.get("/users/")
# def get_users():
#     cursor.execute("SELECT * FROM users")
#     return cursor.fetchall()

# @app.get("/users/{user_id}")
# def get_user(user_id: int):
#     cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
#     user = cursor.fetchone()
#     if user:
#         return user
#     raise HTTPException(status_code=404, detail="User not found")

# @app.put("/users/{user_id}")
# def update_user(user_id: int, user: User):
#     query = "UPDATE users SET name = %s, email = %s WHERE id = %s"
#     cursor.execute(query, (user.name, user.email, user_id))
#     conn.commit()
#     return {"message": "User updated"}

# @app.delete("/users/{user_id}")
# def delete_user(user_id: int):
#     cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
#     conn.commit()
#     return {"message": "User deleted"}


from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="jroshan@98",
    database="testdb"
)
cursor = conn.cursor(dictionary=True)

@app.route("/users", methods=["POST"])
def create_user():
    data = request.json
    query = "INSERT INTO users (name, email) VALUES (%s, %s)"
    cursor.execute(query, (data['name'], data['email']))
    conn.commit()
    return jsonify({"message": "User created", "id": cursor.lastrowid})

@app.route("/users", methods=["GET"])
def get_users():
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    return jsonify(users)

@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
    user = cursor.fetchone()
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.json
    query = "UPDATE users SET name = %s, email = %s WHERE id = %s"
    cursor.execute(query, (data['name'], data['email'], user_id))
    conn.commit()
    return jsonify({"message": "User updated"})

@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
    conn.commit()
    return jsonify({"message": "User deleted"})

if __name__ == "__main__":
    app.run(debug=True)
