from queries.crud import create_task, update_task, update_priority, get_tasks, delete_task


def create_tasks():
    task = input("Enter task name: ")
    status = input("Enter task status: ")
    priority = input("Enter priority: ")
    create_task(task, status, priority)
    print("Task created successfully.")


def update_tasks():
    task_id = input("Enter task ID: ")
    priority = input("Enter new priority: ")
    update_task(task_id, priority)
    print("Task updated successfully.")


def delete_tasks():
    task_id = input("Enter task ID: ")
    delete_task(task_id)
    print("Task deleted successfully.")


def get_task_status():
    for task in get_tasks():
        print(f"ID: {task.id}, Task: {task.task}, Status: {task.status}, Priority: {task.priority}")


def update_task_priority():
    task_id = int(input("Enter task ID: "))
    priority = int(input("Enter new priority: "))
    update_priority(task_id, priority)
    print("Task priority updated successfully.")
    print(get_tasks())
