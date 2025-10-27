# main.py
# ============================
# Entry point for the Task Manager app — provides a text-based user interface.

from task_manager_app.input_validator import add_task, view_tasks, update_task, delete_task

def main_menu():
    """Display main menu and handle user actions."""
    while True:
        print("\n📋 Task Manager")
        print("A. Add Task")
        print("B. View Tasks")
        print("C. Update Task")
        print("D. Delete Task")
        print("E. Exit")

        choice = input("👉 Enter your choice: ").strip().upper()

        if choice == "A":
            add_task()
        elif choice == "B":
            view_tasks()
        elif choice == "C":
            update_task()
        elif choice == "D":
            delete_task()
        elif choice == "E":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    start = input("Start Task Manager? (y/n): ").lower()
    if start == "y":
        main_menu()
    else:
        print("👋 Exiting program.")
