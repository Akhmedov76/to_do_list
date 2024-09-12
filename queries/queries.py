from Decorator.decorator import log_decorator
from queries.crud import create_task, update_task, update_priority, get_tasks, delete_task


@log_decorator
def create_tasks():
    """Create a list of tasks"""
    task = input("Enter task name: ")
    status = input("Enter task status: ")
    priority = input("Enter priority: ")
    create_task(task, status, priority)
    print("Task created successfully.")


@log_decorator
def update_tasks():
    """Update a list of tasks"""
    task_id = input("Enter task ID: ")
    priority = input("Enter new priority: ")
    update_task(task_id, priority)
    print("Task updated successfully.")


@log_decorator
def delete_tasks():
    """Delete a list of tasks"""
    task_id = input("Enter task ID: ")
    delete_task(task_id)
    print("Task deleted successfully.")


@log_decorator
def get_task_status():
    """Return task status information"""
    for task in get_tasks():
        print(f"ID: {task.id}, Task: {task.task}, Status: {task.status}, Priority: {task.priority}")


@log_decorator
def update_task_priority():
    """
    Update task priority
    """
    task_id = input("Enter task ID: ")
    priority = input("Enter new priority: ")
    update_priority(task_id, priority)
    print("Task priority updated successfully.")
    print(get_tasks())
