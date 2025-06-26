from flask import Flask, jsonify, request, abort, make_response, url_for, redirect, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

tasks = [
    {"id": 1, "title": "Buy groceries", "done": False},
    {"id": 2, "title": "Read book", "done": True}
]

@app.route('/')
def index():
    return jsonify(tasks)
    #return render_template('index.html')

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    new_task = {
        "id": len(tasks) + 1,
        "title": data.get("title"),
        "done": False
    }
    tasks.append(new_task)
    return jsonify(new_task), 201

@app.route('/tasks/<int:task_id>', methods=['PATCH'])
def mark_done(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = not task["done"]
            return jsonify(task)
    return jsonify({"error": "Task not found"}), 404

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    return jsonify({"message": "Deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)
