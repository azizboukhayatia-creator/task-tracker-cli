import sys
import json
import os
from datetime import datetime

FILE_NAME = "tasks.json"


def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            tasks = json.load(file)

            if not isinstance(tasks, list):
                print("Error: tasks.json must contain a list.")
                return []

            return tasks

    except json.JSONDecodeError:
        print("Error: tasks.json contains invalid JSON.")
        return []


def save_tasks(tasks):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4, ensure_ascii=False)


def add_task(description):
    tasks = load_tasks()

    # Générer un nouvel ID
    if len(tasks) == 0:
        new_id = 1
    else:
        new_id = max(task["id"] for task in tasks) + 1

    now = datetime.now().isoformat(timespec="seconds")

    task = {
        "id": new_id,
        "description": description,
        "status": "todo",
        "createdAt": now,
        "updatedAt": now
    }

    tasks.append(task)

    save_tasks(tasks)

    print(f"Task added successfully (ID: {new_id})")


def list_tasks(status=None):
    tasks = load_tasks()

    if len(tasks) == 0:
        print("No tasks found.")
        return

    if status is not None:
        tasks = [task for task in tasks if task["status"] == status]

    if len(tasks) == 0:
        print("No tasks found.")
        return

    for task in tasks:
        print(
            f"ID: {task['id']} | "
            f"{task['description']} | "
            f"{task['status']}"
        )


def update_task(task_id, new_description):
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_description
            task["updatedAt"] = datetime.now().isoformat(timespec="seconds")

            save_tasks(tasks)

            print(f"Task updated successfully (ID: {task_id})")
            return

    print(f"Error: task with ID {task_id} not found.")

def delete_task(task_id):
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            save_tasks(tasks)

            print(f"Task deleted successfully (ID: {task_id})")
            return

    print(f"Error: task with ID {task_id} not found.")
 
def mark_in_progress(task_id):
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "in-progress"
            task["updatedAt"] = datetime.now().isoformat(timespec="seconds")

            save_tasks(tasks)

            print(f"Task marked as in-progress (ID: {task_id})")
            return

    print(f"Error: task with ID {task_id} not found.")   
def mark_done(task_id):
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "done"
            task["updatedAt"] = datetime.now().isoformat(timespec="seconds")

            save_tasks(tasks)

            print(f"Task marked as done (ID: {task_id})")
            return

    print(f"Error: task with ID {task_id} not found.")   
def main():
    if len(sys.argv) < 2:
        print("Error: no command provided.")
        return

    command = sys.argv[1]

    if command == "add":

        if len(sys.argv) < 3:
            print("Error: task description is required.")
            return

        description = sys.argv[2]

        if description.strip() == "":
            print("Error: task description cannot be empty.")
            return

        add_task(description)

    elif command == "list":

        if len(sys.argv) == 2:
            list_tasks()

        elif len(sys.argv) == 3:

            status = sys.argv[2]

            if status not in ["todo", "in-progress", "done"]:
                print("Error: invalid status.")
                return

            list_tasks(status)

        else:
            print("Error: invalid number of arguments.")

    elif command == "update":

        if len(sys.argv) != 4:
            print("Error: update requires an ID and a description.")
            return

        try:
            task_id = int(sys.argv[2])
        except ValueError:
            print("Error: ID must be an integer.")
            return

        new_description = sys.argv[3]

        if new_description.strip() == "":
            print("Error: task description cannot be empty.")
            return

        update_task(task_id, new_description)
    elif command == "delete":

        if len(sys.argv) != 3:
            print("Error: delete requires an ID.")
            return

        try:
            task_id = int(sys.argv[2])
        except ValueError:
            print("Error: ID must be an integer.")
            return

        delete_task(task_id)
        
    elif command == "mark-in-progress":

        if len(sys.argv) != 3:
            print("Error: mark-in-progress requires an ID.")
            return

        try:
            task_id = int(sys.argv[2])
        except ValueError:
            print("Error: ID must be an integer.")
            return

        mark_in_progress(task_id)
    elif command == "mark-done":
        if len(sys.argv) != 3:
            print("Error: mark-done requires an ID.")
            return

        try:
            task_id = int(sys.argv[2])
        except ValueError:
            print("Error: ID must be an integer.")
            return

        mark_done(task_id)
    else:
        print(f"Error: unknown command '{command}'.")


if __name__ == "__main__":
    main()
