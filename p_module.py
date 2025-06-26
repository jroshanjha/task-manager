import requests

# Create user
res = requests.post("http://localhost:8000/users/", json={
    "name": "Bob",
    "email": "bob@example.com"
})
print(res.json())

# Get all users
res = requests.get("http://localhost:8000/users/")
print(res.json())

# Get one user
res = requests.get("http://localhost:8000/users/1")
print(res.json())

# Update user
res = requests.put("http://localhost:8000/users/1", json={
    "name": "Bob Updated",
    "email": "bob.updated@example.com"
})
print(res.json())

# Delete user
res = requests.delete("http://localhost:8000/users/1")
print(res.json())
