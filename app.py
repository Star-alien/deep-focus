from flask import Flask, jsonify, request
from models import predict_task_priority, analyze_focus_logs, generate_synthetic_tasks, generate_synthetic_focus_logs, generate_synthetic_iot_data

app = Flask(__name__)

# Generate synthetic data
tasks_data = generate_synthetic_tasks()
focus_logs_data = generate_synthetic_focus_logs()
iot_data = generate_synthetic_iot_data()

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
