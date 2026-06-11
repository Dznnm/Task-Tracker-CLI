import json
import sys

print(sys.argv)

tasks = [
    {
        "id": 0,
        "description": "Learn Flask",
        "status": "todo"
    }
]

if sys.argv[1] == "add":
    tasks[0]["id"] = len(tasks) + 1
    tasks[0]["description"] = sys.argv[2]
    tasks[0]["status"] = "todo"
    print("Task added to memory!")
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)