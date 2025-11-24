
import task_manager
import file_handler

FILENAME = 'tasks.csv'

def main():
    tasks = file_handler.load_tasks(FILENAME)
    while True:
        print("\n===== To-Do List Menu =====")
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. Edit Task")
        print("4. Delete Task")
        print("5. Mark Task as Complete")
        print("6. Mark Task as Incomplete")
        print("7. Exit")
        choice = input("Enter your choice (1-7): ")

        try:
            choice = int(choice)
        except ValueError:
            print("Invalid choice. Please enter a number from 1 to 7.")
            continue

        if choice == 1:
            task_manager.add_task(tasks)
            file_handler.save_tasks(FILENAME, tasks)
        elif choice == 2:
            task_manager.view_tasks(tasks)
        elif choice == 3:
            task_manager.edit_task(tasks)
            file_handler.save_tasks(FILENAME, tasks)
        elif choice == 4:
            task_manager.delete_task(tasks)
            file_handler.save_tasks(FILENAME, tasks)
        elif choice == 5:
            task_manager.mark_complete(tasks)
            file_handler.save_tasks(FILENAME, tasks)
        elif choice == 6:
            task_manager.mark_incomplete(tasks)
            file_handler.save_tasks(FILENAME, tasks)
        elif choice == 7:
            print("Saving tasks and exiting...")
            file_handler.save_tasks(FILENAME, tasks)
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
