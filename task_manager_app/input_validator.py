# input_validator.py
# ============================
# Core logic for adding, viewing, updating, and deleting tasks.
# Includes simple input validation for reliability.

import re
from task_manager_app.file_handler import read_tasks, write_tasks
from task_manager_app.task import Task

PRIORITY_PATTERN = re.compile(r'^(High|Medium|Low)$', re.I)

def _valid_text(value: str) -> bool:
    return bool(value and value.strip())

def _valid_priority(value: str) -> bool:
    return bool(PRIORITY_PATTERN.match(value.strip()))

def add_task():
    """Add a new task to the list after validation."""
    name = input("Enter task name: ").strip()
    if not _valid_text(name):
        print("❌ Invalid name.")
        return

    description = input("Enter task description: ").strip()
    if not _valid_text(description):
        print("❌ Invalid description.")
        return

    priority = input("Enter priority (High/Medium/Low): ").strip().capitalize()
    if not _valid_priority(priority):
        print("❌ Invalid priority.")
        return

    tasks = read_tasks()
    tasks.append(Task(name, description, priority))
    write_tasks(tasks)
    print("✅ Task added successfully!")

def view_tasks():
    """Display all current tasks."""
    tasks = read_tasks()
    if not tasks:
        print("📭 No tasks available.")
        return
    print("\n🗂️ Your Tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def update_task():
    """Update an existing task."""
    tasks = read_tasks()
    if not tasks:
        print("📭 No tasks to update.")
        return

    view_tasks()
    try:
        idx = int(input("Enter task number to update: ")) - 1
    except ValueError:
        print("❌ Invalid number.")
        return

    if idx < 0 or idx >= len(tasks):
        print("❌ Invalid task number.")
        return

    old = tasks[idx]
    print(f"\nEditing Task: {old.name}\n1) Name: {old.name}\n2) Description: {old.description}\n3) Priority: {old.priority}")
    choice = input("Select field to edit (1-3) or 4 to cancel: ").strip()

    if choice == "1":
        new_name = input("Enter new name: ").strip()
        if not _valid_text(new_name):
            print("❌ Invalid name.")
            return
        tasks[idx].name = new_name
    elif choice == "2":
        new_desc = input("Enter new description: ").strip()
        if not _valid_text(new_desc):
            print("❌ Invalid description.")
            return
        tasks[idx].description = new_desc
    elif choice == "3":
        new_pr = input("Enter new priority (High/Medium/Low): ").strip().capitalize()
        if not _valid_priority(new_pr):
            print("❌ Invalid priority.")
            return
        tasks[idx].priority = new_pr
    elif choice == "4":
        print("❌ Update cancelled.")
        return
    else:
        print("❌ Invalid choice.")
        return

    write_tasks(tasks)
    print("✅ Task updated successfully!")

def delete_task():
    """Delete a task by index."""
    tasks = read_tasks()
    if not tasks:
        print("📭 No tasks to delete.")
        return

    view_tasks()
    try:
        idx = int(input("Enter task number to delete: ")) - 1
    except ValueError:
        print("❌ Invalid number.")
        return

    if idx < 0 or idx >= len(tasks):
        print("❌ Invalid task number.")
        return

    confirm = input(f"Delete '{tasks[idx].name}'? (y/n): ").strip().lower()
    if confirm == "y":
        tasks.pop(idx)
        write_tasks(tasks)
        print("✅ Task deleted successfully!")
    else:
        print("❌ Deletion cancelled.")
