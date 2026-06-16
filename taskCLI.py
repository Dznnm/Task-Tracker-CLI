import json
import sys

if sys.argv[1] == "add":
    with open("tasks.json", "r") as file:
        tasks = json.load(file)
    highest_id = max(task["id"] for task in tasks) if tasks else 0
    new_task = {
        "id": highest_id + 1,
        "description": sys.argv[2],
        "status": "To Do"
    }
    tasks.append(new_task)
    print("Task added to memory!")
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

if sys.argv[1] == "list":
    with open("tasks.json", "r") as file:
        tasks = json.load(file)
    for task in tasks:
        print(f"{task['id']}: {task['description']} - {task['status']}")

if sys.argv[1] == "update":
    with open("tasks.json", "r") as file:
        tasks = json.load(file)
    for task in tasks:
        if task["id"] == int(sys.argv[2]):
            task["status"] = sys.argv[3]
            print("Task updated!")
            break
    else:
            print("Task not found!")
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

if sys.argv[1] == "delete":
    with open("tasks.json", "r") as file:
        tasks = json.load(file)
    for task in tasks:
        if task["id"] == int(sys.argv[2]):
            tasks.remove(task)
            print("Task deleted!")
            break
    else:
        print("Task not found!")
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

if sys.argv[1] == "mark-done":
    with open("tasks.json", "r") as file:
        tasks = json.load(file)
    for task in tasks:
        if task["id"] == int(sys.argv[2]):
            task["status"] = "Done"
            print("Task Completed!")
            break
    else:
            print("Task not found!")
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

if sys.argv[1] == "mark-WIP":
    with open("tasks.json", "r") as file:
        tasks = json.load(file)
    for task in tasks:
        if task["id"] == int(sys.argv[2]):
            task["status"] = "In Progress"
            print("Task In-Progress!")
            break
    else:
            print("Task not found!")
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)