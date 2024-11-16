import json
import os
from faker import Faker
import random

DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)

fake = Faker()

# Generate synthetic tasks
tasks = [{"id": i, "description": fake.sentence(), "status": random.choice(["Pending", "Completed"])} for i in range(50)]
with open(os.path.join(DATA_DIR, "tasks.json"), "w") as f:
    json.dump(tasks, f, indent=4)

# Generate synthetic focus logs
focus_logs = [{"id": i, "timestamp": fake.date_time_this_month().isoformat(), "status": random.choice(["Focused", "Distracted"])} for i in range(100)]
with open(os.path.join(DATA_DIR, "focus_logs.json"), "w") as f:
    json.dump(focus_logs, f, indent=4)

# Generate synthetic IoT data
iot_data = [{"device_id": f"device_{i}", "temperature": random.uniform(18.0, 30.0), "humidity": random.uniform(30.0, 70.0), "status": random.choice(["Online", "Offline"])} for i in range(20)]
with open(os.path.join(DATA_DIR, "iot_mock.json"), "w") as f:
    json.dump(iot_data, f, indent=4)

print("Synthetic data generated and saved in the data/ directory.")
