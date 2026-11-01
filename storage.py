import json
import os

DATA_FILE = "tasks.json"

def load():
    """Load tasks from the tasks.json file. Returns an empty list if the file doesn't exist or is empty."""
    if not os.path.exists(DATA_FILE):
        return []
    
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            content = f.read().strip()
            if not content:
                return []
            return json.loads(content)
    except (json.JSONDecodeError, IOError):
        return []

def save(tasks):
    """Save the given tasks list to the tasks.json file in a single line."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2)