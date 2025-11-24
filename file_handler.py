
import csv

def load_tasks(filename):
    tasks = []
    try:
        with open(filename, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                task = {
                    'id': int(row['id']),
                    'title': row['title'],
                    'description': row['description'],
                    'due_date': row['due_date'],
                    'status': row['status']
                }
                tasks.append(task)
    except FileNotFoundError:
        return tasks
    except Exception as e:
        print("Error loading tasks:", e)
    return tasks

def save_tasks(filename, tasks):
    try:
        with open(filename, mode='w', newline='') as file:
            fieldnames = ['id', 'title', 'description', 'due_date', 'status']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for task in tasks:
                writer.writerow(task)
    except Exception as e:
        print("Error saving tasks:", e)
