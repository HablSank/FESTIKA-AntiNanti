import json
import sys
import datetime
import os

TASK_FILE = "tasks.json"

def load_tasks():
    """Memuat daftar tugas dari file JSON."""
    if not os.path.exists(TASK_FILE):
        return []
    try:
        with open(TASK_FILE, 'r') as f:
            tasks = json.load(f)
            return tasks
    except json.JSONDecodeError:
        print(f"Error: File {TASK_FILE} rusak atau tidak valid.")
        return []
    
def save_tasks(tasks_list):
    try:
        with open(TASK_FILE, 'w') as f:
            json.dump(tasks_list, f, indent=4)
    except IOError as e:
        print(f"Error saat menyimpan file: {e}")
