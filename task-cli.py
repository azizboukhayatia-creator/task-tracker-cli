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


def add_task(description, priority, category, estimated_minutes):
    tasks = load_tasks()

    if len(tasks) == 0:
        new_id = 1
    else:
        new_id = max(task["id"] for task in tasks) + 1

    now = datetime.now().isoformat(timespec="seconds")

    task = {
        "id": new_id,
        "description": description,
        "status": "todo",
        "priority": priority,
        "category": category,
        "estimatedMinutes": estimated_minutes,
        "actualMinutes": None,
        "createdAt": now,
        "updatedAt": now,
        "completedAt": None
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
        estimated = task["estimatedMinutes"]
        actual = task["actualMinutes"]

        if actual is None:
            actual_display = "-"
            difference_display = "-"
            efficiency_display = "-"
        else:
            actual_display = f"{actual} min"

            difference = actual - estimated

            if difference > 0:
                difference_display = f"+{difference} min"
            elif difference < 0:
                difference_display = f"{difference} min"
            else:
                difference_display = "0 min"

            efficiency = (estimated / actual) * 100
            efficiency_display = f"{efficiency:.1f}%"

        print(
            f"ID: {task['id']} | "
            f"{task['description']} | "
            f"{task['status']} | "
            f"Priority: {task['priority']} | "
            f"Category: {task['category']} | "
            f"Estimated: {estimated} min | "
            f"Actual: {actual_display} | "
            f"Difference: {difference_display} | "
            f"Efficiency: {efficiency_display}"
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


def mark_done(task_id, actual_minutes):
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == task_id:
            completed_at = datetime.now().isoformat(timespec="seconds")

            task["status"] = "done"
            task["actualMinutes"] = actual_minutes
            task["completedAt"] = completed_at
            task["updatedAt"] = completed_at

            save_tasks(tasks)

            print(f"Task marked as done (ID: {task_id})")
            return

    print(f"Error: task with ID {task_id} not found.")

def main():
    if len(sys.argv) < 2:
        print("Error: no command provided.")
        return

    command = sys.argv[1]

    # ADD
    if command == "add":

        if len(sys.argv) != 6:
            print(
                "Error: add requires description, "
                "priority, category and estimated time."
            )
            return

        description = sys.argv[2]
        priority = sys.argv[3]
        category = sys.argv[4]
        if priority not in ["low", "medium", "high"]:
            print("Error: priority must be low, medium or high.")
            return

        if category not in ["study", "work", "personal", "project", "other"]:
            print("Error: invalid category.")
            return
        try:
            estimated_minutes = int(sys.argv[5])
        except ValueError:
            print("Error: estimated time must be an integer.")
            return
        if estimated_minutes <= 0:
            print("Error: estimated time must be greater than 0.")
            return
        if description.strip() == "":
            print("Error: task description cannot be empty.")
            return

        add_task(
            description,
            priority,
            category,
            estimated_minutes
        )

    # LIST
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

    # UPDATE
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

    # DELETE
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

    # MARK IN PROGRESS
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

    # MARK DONE
    elif command == "mark-done":

        if len(sys.argv) != 4:
            print("Error: mark-done requires an ID and actual time.")
            return

        try:
            task_id = int(sys.argv[2])
        except ValueError:
            print("Error: ID must be an integer.")
            return

        try:
            actual_minutes = int(sys.argv[3])
        except ValueError:
            print("Error: actual time must be an integer.")
            return

        if actual_minutes <= 0:
            print("Error: actual time must be greater than 0.")
            return

        mark_done(task_id, actual_minutes)

    else:
        print(f"Error: unknown command '{command}'.")


if __name__ == "__main__":
    main()