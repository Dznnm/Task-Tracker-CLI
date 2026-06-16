# Task Tracker CLI

A simple command-line task tracker built with Python and JSON storage.

Project URL:
https://roadmap.sh/projects/task-tracker

## Features

* Add tasks
* List all tasks
* Filter tasks by status
* Update task status
* Mark tasks as done
* Mark tasks as in progress
* Delete tasks
* Store tasks in JSON format
* Track creation and update timestamps

## Requirements

* Python 3.x

No external libraries required.

## Usage

### Add a task

```bash
python taskCLI.py add "Learn Python"
```

### List all tasks

```bash
python taskCLI.py list
```

### List tasks by status

```bash
python taskCLI.py list todo
python taskCLI.py list WIP
python taskCLI.py list done
```

### Update a task status

```bash
python taskCLI.py update 1 Done
```

### Mark task as done

```bash
python taskCLI.py mark-done 1
```

### Mark task as in progress

```bash
python taskCLI.py mark-WIP 1
```

### Delete a task

```bash
python taskCLI.py delete 1
```

## Storage

Tasks are stored in:

```txt
tasks.json
```

Example:

```json
{
    "id": 1,
    "description": "Learn Python",
    "status": "Done",
    "created at": "2026-06-16 22:00:00",
    "updated at": "2026-06-16 22:30:00"
}
```

## Author

Dzannun Muhlashon (future tech wizz)
