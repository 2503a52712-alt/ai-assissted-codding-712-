# Initial version
tasks = []

def add_task(task):
    tasks.append(task)

def show_tasks():
    for number, task in enumerate(tasks, start=1):
        print(f"{number}. {task}")

add_task("Complete lab")
add_task("Review code")
show_tasks()

# Improved version with validation and task completion
tasks = []

def add_task(task):
    task = task.strip()
    if not task:
        print("Task cannot be empty.")
        return
    tasks.append({"text": task, "done": False})
    print("Task added.")

def show_tasks():
    if not tasks:
        print("No tasks yet.")
        return

    for number, task in enumerate(tasks, start=1):
        status = "Done" if task["done"] else "Not done"
        print(f"{number}. {task['text']} [{status}]")

def complete_task(number):
    if 1 <= number <= len(tasks):
        tasks[number - 1]["done"] = True
        print("Task marked as done.")
    else:
        print("Invalid task number.")

add_task("Complete lab")
add_task("Review code")
complete_task(1)
show_tasks()