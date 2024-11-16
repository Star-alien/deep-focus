from flask import Flask, jsonify, request
import json
import os
from models import predict_task_priority, analyze_focus_logs

app = Flask(__name__)

# Load synthetic data
DATA_DIR = "data"
tasks_file = os.path.join(DATA_DIR, "tasks.json")
focus_logs_file = os.path.join(DATA_DIR, "focus_logs.json")
iot_file = os.path.join(DATA_DIR, "iot_mock.json")

with open(tasks_file, "r") as f:
    tasks_data = json.load(f)

with open(focus_logs_file, "r") as f:
    focus_logs_data = json.load(f)

with open(iot_file, "r") as f:
    iot_data = json.load(f)

@app.route("/")
def home():
    return jsonify({"message": "Backend is running!"})

# API to get all tasks
@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks_data)

# API to analyze task priority
@app.route("/tasks/predict", methods=["POST"])
def predict_priority():
    task = request.json.get("task")
    if not task:
        return jsonify({"error": "Task description is required"}), 400
    
    priority = predict_task_priority(task)
    return jsonify({"task": task, "predicted_priority": priority})

# API to analyze focus logs
@app.route("/focus_logs/analyze", methods=["GET"])
def analyze_focus():
    insights = analyze_focus_logs(focus_logs_data)
    return jsonify(insights)

# API to get IoT data
@app.route("/iot_data", methods=["GET"])
def get_iot_data():
    return jsonify(iot_data)

if __name__ == "__main__":
    app.run(debug=True)
