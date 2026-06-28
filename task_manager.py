import json
import os
import uuid

FILE_NAME = "task.json"


def load_tasks():
    """
    Load all tasks from task.json
    """

    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []


def save_tasks(tasks):
    """
    Save all tasks to task.json
    """

    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(title):
    """
    Add a new task
    """

    tasks = load_tasks()

    task = {
        "id": str(uuid.uuid4()),
        "title": title,
        "completed": False
    }

    tasks.append(task)

    save_tasks(tasks)


def mark_completed(task_id):
    """
    Mark task as completed
    """

    tasks = load_tasks()

    for task in tasks:

        if task["id"] == task_id:
            task["completed"] = True
            break

    save_tasks(tasks)


def mark_pending(task_id):
    """
    Move completed task back to pending
    """

    tasks = load_tasks()

    for task in tasks:

        if task["id"] == task_id:
            task["completed"] = False
            break

    save_tasks(tasks)


def delete_task(task_id):
    """
    Delete task
    """

    tasks = load_tasks()

    tasks = [
        task
        for task in tasks
        if task["id"] != task_id
    ]

    save_tasks(tasks)


def get_pending_tasks():
    """
    Return only pending tasks
    """

    tasks = load_tasks()

    return [
        task
        for task in tasks
        if not task["completed"]
    ]


def get_completed_tasks():
    """
    Return only completed tasks
    """

    tasks = load_tasks()

    return [
        task
        for task in tasks
        if task["completed"]
    ]