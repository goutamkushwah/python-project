import json
import sys
import os
from datetime import datetime

FILE_NAME = "tasks.json"


def load_tasks():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w") as file:
            json.dump([], file)

    with open(FILE_NAME, "r") as file:
        return json.load(file)


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(description):
    tasks = load_tasks()

    new_id = 1
    if tasks:
        new_id = max(task["id"] for task in tasks) + 1

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    task = {
        "id": new_id,
        "description": description,
        "status": "todo",
        "createdAt": current_time,
        "updatedAt": current_time
    }

    tasks.append(task)
    save_tasks(tasks)

    print(f"Task added successfully (ID: {new_id})")


def update_task(task_id, description):
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == task_id:
            task["description"] = description
            task["updatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_tasks(tasks)
            print("Task updated successfully")
            return

    print("Task not found")


def delete_task(task_id):
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            save_tasks(tasks)
            print("Task deleted successfully")
            return

    print("Task not found")


def mark_task(task_id, status):
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == task_id:
            task["status"] = status
            task["updatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_tasks(tasks)
            print(f"Task marked as {status}")
            return

    print("Task not found")


def list_tasks(status=None):
    tasks = load_tasks()

    if status:
        tasks = [task for task in tasks if task["status"] == status]

    if not tasks:
        print("No tasks found")
        return

    print("-" * 80)
    print(f"{'ID':<5}{'DESCRIPTION':<30}{'STATUS':<15}")
    print("-" * 80)

    for task in tasks:
        print(
            f"{task['id']:<5}"
            f"{task['description']:<30}"
            f"{task['status']:<15}"
        )


def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("python task.py add \"Task Description\"")
        return

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3:
            print("Please provide a task description")
            return

        add_task(sys.argv[2])

    elif command == "update":
        if len(sys.argv) < 4:
            print("Usage: python task.py update <id> <description>")
            return

        update_task(int(sys.argv[2]), sys.argv[3])

    elif command == "delete":
        if len(sys.argv) < 3:
            print("Usage: python task.py delete <id>")
            return

        delete_task(int(sys.argv[2]))

    elif command == "mark-in-progress":
        if len(sys.argv) < 3:
            print("Usage: python task.py mark-in-progress <id>")
            return

        mark_task(int(sys.argv[2]), "in-progress")

    elif command == "mark-done":
        if len(sys.argv) < 3:
            print("Usage: python task.py mark-done <id>")
            return

        mark_task(int(sys.argv[2]), "done")

    elif command == "list":
        if len(sys.argv) == 2:
            list_tasks()
        else:
            list_tasks(sys.argv[2])

    else:
        print("Invalid command")


if __name__ == "__main__":
    main()