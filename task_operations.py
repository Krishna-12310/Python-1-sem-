import task_data
from date_utils import validate_date


def add_task():
    name = input("Enter task name: ").strip()
    assigned_to = input("Enter team member name: ").strip()

    if not name or not assigned_to:
        print("Task name and team member cannot be empty!")
        return

    due_date = input("Enter due date (YYYY-MM-DD): ").strip()

    if not validate_date(due_date):
        print("Invalid date! Use YYYY-MM-DD format.")
        return

    print("Available Task IDs:", list(task_data.tasks.keys()))

    dependency = input("Enter dependency Task ID (0 for none): ")

    try:
        dependency = int(dependency)
    except ValueError:
        print("Please enter a valid Task ID!")
        return

    if dependency < 0:
        print("Task ID cannot be negative!")
        return

    if dependency != 0 and dependency not in task_data.tasks:
        print("Invalid dependency ID!")
        return

    dependencies = []

    if dependency != 0:
        dependencies.append(dependency)

    current_id = task_data.task_id

    task_data.tasks[current_id] = {
        "name": name,
        "assigned_to": assigned_to,
        "due_date": due_date,
        "status": "Pending",
        "dependencies": dependencies
    }

    print("Task added successfully!")
    print("Task ID:", current_id)

    task_data.task_id += 1


def update_task():
    try:
        task_number = int(input("Enter Task ID: "))
    except ValueError:
        print("Please enter a valid Task ID!")
        return

    if task_number not in task_data.tasks:
        print("Task not found!")
        return

    print("1. Pending")
    print("2. In Progress")
    print("3. Completed")

    choice = input("Enter new status: ")

    if choice not in ["1", "2", "3"]:
        print("Invalid choice!")
        return

    if choice in ["2", "3"]:
        for dependency in task_data.tasks[task_number]["dependencies"]:
            if task_data.tasks[dependency]["status"] != "Completed":
                print("This task is BLOCKED!")
                print("Complete Task ID", dependency, "first.")
                return

    if choice == "1":
        task_data.tasks[task_number]["status"] = "Pending"
    elif choice == "2":
        task_data.tasks[task_number]["status"] = "In Progress"
    else:
        task_data.tasks[task_number]["status"] = "Completed"

    print("Task status updated successfully!")