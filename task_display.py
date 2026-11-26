from task_data import tasks
from date_utils import is_overdue


def view_tasks():
    if not tasks:
        print("No tasks available!")
        return

    for task_id, task in tasks.items():
        print("\n-----------------------------")
        print("Task ID:", task_id)
        print("Task Name:", task["name"])
        print("Assigned To:", task["assigned_to"])
        print("Due Date:", task["due_date"])
        print("Status:", task["status"])
        print("Dependencies:", task["dependencies"])

        blocked = False

        for dependency in task["dependencies"]:
            if tasks[dependency]["status"] != "Completed":
                blocked = True

        overdue = is_overdue(task["due_date"], task["status"])

        if blocked:
            print("Task Condition: BLOCKED")

        if overdue:
            print("Task Condition: OVERDUE")

        if not blocked and not overdue:
            print("Task Condition: Normal")


def view_blocked_tasks():
    found = False

    print("\n========== BLOCKED TASKS ==========")

    for task_id, task in tasks.items():
        for dependency in task["dependencies"]:
            if tasks[dependency]["status"] != "Completed":
                print("Task ID:", task_id)
                print("Task Name:", task["name"])
                print("Blocked By Task ID:", dependency)
                found = True
                break

    if not found:
        print("No blocked tasks!")


def view_overdue_tasks():
    found = False

    print("\n========== OVERDUE TASKS ==========")

    for task_id, task in tasks.items():
        if is_overdue(task["due_date"], task["status"]):
            print("Task ID:", task_id)
            print("Task Name:", task["name"])
            print("Assigned To:", task["assigned_to"])
            print("Due Date:", task["due_date"])
            found = True

    if not found:
        print("No overdue tasks!")
       