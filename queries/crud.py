from sqlalchemy import desc

from Decorator.decorator import log_decorator
from database.database import execute_query
from queries.models import tasks

@log_decorator
def create_task(task, status, priority):
    """
    Create a new task.
    """
    query = tasks.insert().values(task=task, status=status, priority=priority)
    result = execute_query(query=query)
    return result.inserted_primary_key

@log_decorator
def get_task(task_id):
    """
    Retrieve a task by its ID.
    """
    query = tasks.select().where(tasks.c.id == task_id)
    result = execute_query(query=query, )
    return result.fetchone()

@log_decorator
def get_tasks(descending=False):
    """
    Retrieve all tasks.
    """
    if descending:
        query = tasks.select().order_by(desc(tasks.c.priority))
    else:
        query = tasks.select()
    result = execute_query(query=query, )
    return result.fetchall()

@log_decorator
def update_task(task_id, priority, ):
    """
    Update the priority of a task.
    """
    query = tasks.update().where(tasks.c.id == task_id).values(priority)
    result = execute_query(query=query)
    return result.rowcount

@log_decorator
def delete_task(task_id):
    """
    Delete a task by its ID.
    """
    query = tasks.delete().where(tasks.c.id == task_id)
    result = execute_query(query=query)
    return result.rowcount

@log_decorator
def update_priority(task_id, priority):
    """
    Update the priority of a task.
    """
    changed_tasks = get_task(task_id=task_id)
    if changed_tasks[3] == priority:
        return True
    else:
        all_task = get_tasks()
        for task in all_task:
            if priority > changed_tasks[3]:
                update_task(task_id=task[0], priority=task[3] - 1)
            else:
                update_task(task_id=task[0], priority=task[3] + 1)
        update_task(task_id=task_id, priority=priority)
