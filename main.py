import threading

from queries.models import create_to_do_list_table
from queries.queries import create_tasks, update_tasks, delete_tasks, get_task_status, update_task_priority


def auth_menu():
    print("""
1. Create a new task
2. Edit the task
3. Delete the task
4. Show all tasks
5. Task switching
6. Logout
    """)
    choice = input("Enter your choice: ")
    if choice == "1":
        create_tasks()
        auth_menu()
    elif choice == "2":
        update_tasks()
        auth_menu()
    elif choice == "3":
        delete_tasks()
        auth_menu()
    elif choice == "4":
        get_task_status()
        auth_menu()
    elif choice == "5":
        update_task_priority()
        auth_menu()
    elif choice == "6":
        print("Goodbye!")
        exit(0)
    else:
        print("Invalid choice, please try again!")
        auth_menu()


if __name__ == "__main__":
    threading.Thread(target=create_to_do_list_table()).start()
    auth_menu()
