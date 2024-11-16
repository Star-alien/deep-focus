import random
import json
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Task priority prediction model (dummy trained model for demonstration)
def predict_task_priority(task):
    # Simulate a simple prediction using random logic
    priorities = ["High", "Medium", "Low"]
    return random.choice(priorities)

# Focus logs analysis model
def analyze_focus_logs(focus_logs):
    total_logs = len(focus_logs)
    distracted_count = sum(1 for log in focus_logs if log["status"] == "Distracted")
    focused_count = total_logs - distracted_count

    return {
        "total_logs": total_logs,
        "focused_logs": focused_count,
        "distracted_logs": distracted_count,
        "focus_percentage": round((focused_count / total_logs) * 100, 2),
    }

# Function to generate synthetic tasks data
def generate_synthetic_tasks(num_tasks=10):
    tasks = []
    for i in range(num_tasks):
        task_description = f"Task {i+1} description"
        priority = random.choice(["High", "Medium", "Low"])
        tasks.append({
            "task_id": i+1,
            "task_description": task_description,
            "priority": priority
        })
    return tasks

# Function to generate synthetic focus logs data
def generate_synthetic_focus_logs(num_logs=10):
    statuses = ["Focused", "Distracted"]
    focus_logs = []
    for i in range(num_logs):
        focus_logs.append({
            "log_id": i+1,
            "status": random.choice(statuses),
            "timestamp": f"2024-11-16T10:00:{i:02d}"
        })
    return focus_logs

# Function to generate synthetic IoT data (example)
def generate_synthetic_iot_data(num_records=10):
    iot_data = []
    for i in range(num_records):
        iot_data.append({
            "sensor_id": f"sensor_{i+1}",
            "temperature": random.uniform(20, 30),
            "humidity": random.uniform(30, 60),
            "timestamp": f"2024-11-16T10:00:{i:02d}"
        })
    return iot_data
