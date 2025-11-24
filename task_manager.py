
def get_next_id(tasks):
    if tasks:
        return max(task['id'] for task in tasks) + 1
    else:
        return 1

def add_task(tasks):
    title = input("Enter task title: ").strip()
    if not title:
        print("Task title cannot be empty.")
        return
    description = input("Enter task description (optional): ").strip()
    due_date = input("Enter due date (YYYY-MM-DD, optional): ").strip()
    new_task = {
        'id': get_next_id(tasks),
        'title': title,
        'description': description,
        'due_date': due_date,
        'status': 'incomplete'
    }
    tasks.append(new_task)
    print("Task added successfully.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks to display.")
        return
    print("\nCurrent Tasks:")
    print("-" * 40)
    for task in tasks:
        print(f"ID: {task['id']}")
        print(f"Title: {task['title']}")
        print(f"Description: {task['description']}")
        print(f"Due Date: {task['due_date']}")
        print(f"Status: {task['status']}")
        print("-" * 40)

def find_task(tasks, task_id):
    for task in tasks:
        if task['id'] == task_id:
            return task
    return None

def edit_task(tasks):
    try:
        task_id = int(input("Enter the ID of the task to edit: "))
    except ValueError:
        print("Invalid ID.")
        return
    task = find_task(tasks, task_id)
    if not task:
        print("Task not found.")
        return
    new_title = input(f"Enter new title (leave blank to keep '{task['title']}'): ").strip()
    if new_title:
        task['title'] = new_title
    new_desc = input("Enter new description (leave blank to keep existing): ").strip()
    if new_desc:
        task['description'] = new_desc
    new_due = input(f"Enter new due date (leave blank to keep '{task['due_date']}'): ").strip()
    if new_due:
        task['due_date'] = new_due
    print("Task updated successfully.")

def delete_task(tasks):
    try:
        task_id = int(input("Enter the ID of the task to delete: "))
    except ValueError:
        print("Invalid ID.")
        return
    task = find_task(tasks, task_id)
    if not task:
        print("Task not found.")
        return
    tasks.remove(task)
    print("Task deleted successfully.")

def mark_complete(tasks):
    try:
        task_id = int(input("Enter the ID of the task to mark as complete: "))
    except ValueError:
        print("Invalid ID.")
        return
    task = find_task(tasks, task_id)
    if not task:
        print("Task not found.")
        return
    task['status'] = 'complete'
    print("Task marked as complete.")

def mark_incomplete(tasks):
    try:
        task_id = int(input("Enter the ID of the task to mark as incomplete: "))
    except ValueError:
        print("Invalid ID.")
        return
    task = find_task(tasks, task_id)
    if not task:
        print("Task not found.")
        return
    task['status'] = 'incomplete'
    print("Task marked as incomplete.")
