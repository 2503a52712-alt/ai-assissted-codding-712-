# Combined result of Student A's and Student B's work

tasks = []

# Student A's initial feature
def add_task(task):
    task = task.strip()
    if not task:
        print("Task cannot be empty.")
        return
    tasks.append({"text": task, "done": False})

def show_tasks():
    if not tasks:
        print("No tasks yet.")
        return

    for number, task in enumerate(tasks, start=1):
        status = "Done" if task["done"] else "Not done"
        print(f"{number}. {task['text']} [{status}]")

# Student B's added feature
def complete_task(number):
    if not isinstance(number, int) or not 1 <= number <= len(tasks):
        print("Invalid task number.")
        return
    tasks[number - 1]["done"] = True
    print("Task marked as done.")

add_task("Write initial version")
add_task("Review improvements")
complete_task(1)
show_tasks()