
# Created Virtual Environments 
python -m venv venv 

# Activate Virtual Environments 
venv/Scripts/activate

# Install dependencies package and libraries 
pip install -r requirements.txt

# ▶️ Run FastAPI:
uvicorn main:app --reload

python -m app.main
uvicorn app.main:app --reload

# Request URL => GET
http://127.0.0.1:8000/users/ 

curl -X 'GET' \
  'http://127.0.0.1:8000/users/' \
  -H 'accept: application/json'
# Response Body
[
  {
    "id": 1,
    "name": "jroshan",
    "email": "jroshan@example.com"
  }
]

# Request URL => POST
http://127.0.0.1:8000/users/

{
  "name": "jroshan",
  "email": "jroshan@example.com"
}

curl -X 'POST' \
  'http://127.0.0.1:8000/users/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "jroshan",
  "email": "jroshan@example.com"
}'

# Response body
{
  "message": "User created",
  "id": 1
}

# Response Headers 
content-length: 33 
content-type: application/json 
date: Thu,26 Jun 2025 15:24:21 GMT 
server: uvicorn 


# Error Message 

{
  "detail": [
    {
      "type": "value_error",
      "loc": [
        "body",
        "name"
      ],
      "msg": "Value error, Name must contain only letters and spaces",
      "input": "user123",
      "ctx": {
        "error": {}
      }
    },
    {
      "type": "value_error",
      "loc": [
        "body",
        "email"
      ],
      "msg": "value is not a valid email address: The part after the @-sign is not valid. It should have a period.",
      "input": "user@examplecom",
      "ctx": {
        "reason": "The part after the @-sign is not valid. It should have a period."
      }
    }
  ]
}


# Request URL => GET
http://127.0.0.1:8000/users/2

curl -X 'GET' \
  'http://127.0.0.1:8000/users/2' \
  -H 'accept: application/json'
	
# Response body

{
  "id": 2,
  "name": "user",
  "email": "user@example.com"
}


# Request URL => PUT 
http://127.0.0.1:8000/users/2

curl -X 'PUT' \
  'http://127.0.0.1:8000/users/2' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "user",
  "email": "user@gmail.com"
}'

# Response Body 
{
  "message": "User updated"
}


# Request URL  => DELETE
http://127.0.0.1:8000/users/5

curl -X 'DELETE' \
  'http://127.0.0.1:8000/users/5' \
  -H 'accept: application/json'

# Response body
{
  "message": "User deleted"
}

# Flask 
http://127.0.0.1:5000


# FAST API 

# CREATE user
curl -X POST "http://localhost:8000/users/" \
-H "Content-Type: application/json" \
-d '{
    "name": "John Doe",
    "email": "john@example.com",
    "age": 30
}'

# GET all users
curl -X GET "http://localhost:8000/users/"

# GET user by ID
curl -X GET "http://localhost:8000/users/1"

# UPDATE user
curl -X PUT "http://localhost:8000/users/1" \
-H "Content-Type: application/json" \
-d '{
    "name": "John Updated",
    "age": 31
}'

# DELETE user
curl -X DELETE "http://localhost:8000/users/1"

Flask API 

# CREATE user
curl -X POST "http://localhost:5000/users" \
-H "Content-Type: application/json" \
-d '{
    "name": "Jane Doe",
    "email": "jane@example.com",
    "age": 25
}'

# GET all users
curl -X GET "http://localhost:5000/users"

# GET user by ID
curl -X GET "http://localhost:5000/users/1"

# UPDATE user
curl -X PUT "http://localhost:5000/users/1" \
-H "Content-Type: application/json" \
-d '{
    "name": "Jane Updated",
    "age": 26
}'

# DELETE user
curl -X DELETE "http://localhost:5000/users/1"