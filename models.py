from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import random

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
