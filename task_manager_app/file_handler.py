# file_handler.py
# ============================
# Handles reading and writing task data to a JSON file for persistence.

import json
from task_manager_app.task import Task

FILE_PATH = "task_manager_app/data/tasks.json"

def read_tasks(filepath=FILE_PATH):
    """Read all tasks from JSON and return as Task objects."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
            return [Task.from_dict(t) for t in data]
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("⚠️ Warning: Could not read tasks — file may be corrupted.")
        return []

def write_tasks(tasks, filepath=FILE_PATH):
    """Write the given list of Task objects to the JSON file."""
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump([t.to_dict() for t in tasks], f, indent=4, ensure_ascii=False)
