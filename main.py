from task_operations import add_task, update_task
from task_display import view_tasks, view_blocked_tasks, view_overdue_tasks


def main():
    while True:
        print("\n================================")
        print("        TEAM TASK BOARD")
        print("================================")
        print("1. Add New Task")
        print("2. Update Task Status")
        print("3. View All Tasks")
        print("4. View Blocked Tasks")
        print("5. View Overdue Tasks")
        print("6. Exit")
        print("================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()

        elif choice == "2":
            update_task()

        elif choice == "3":
            view_tasks()

        elif choice == "4":
            view_blocked_tasks()

        elif choice == "5":
            view_overdue_tasks()

        elif choice == "6":
            print("Thank you for using Team Task Board!")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
    