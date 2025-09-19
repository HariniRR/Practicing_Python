#2.command-line to-do list application where users can add, remove, and view tasks. Store the tasks in a list and allow users to mark tasks as completed.
todo = []
print("📝 Welcome to the To-Do List App!")
while True:
    print("\nChoose an operation:")
    print("1. Add Task")
    print("2. Edit Task")
    print("3. Delete Task")
    print("4. Mark Task as Completed")
    print("5. View Tasks")
    print("6. Exit")
    choice = input("Your choice: ")
    if choice == '1':
        task = input("Enter the task to add: ")
        todo.append({'task': task, 'completed': False})
    elif choice == '2':
        task_to_edit = input("Enter the task to edit: ")
        for item in todo:
            if item['task'] == task_to_edit:
                new_task = input("Enter the new task: ")
                item['task'] = new_task
                break
        else:
            print("Task not found.")
    elif choice == '3':
        task_to_delete = input("Enter the task to delete: ")
        for item in todo:
            if item['task'] == task_to_delete:
                todo.remove(item)
                break
        else:
            print("Task not found.")
    elif choice == '4':
        task_to_complete = input("Enter the task to mark as completed: ")
        for item in todo:
            if item['task'] == task_to_complete:
                item['completed'] = True
                break
        else:
            print("Task not found.")
    elif choice == '5':
        print("\n📋 Current To-Do List:")
        for i, item in enumerate(todo, 1):
            status = "✅" if item['completed'] else "❌"
            print(f"{i}. {item['task']} [{status}]")
    elif choice == '6':
        print("Goodbye! 👋")
        break
    else:
        print("Invalid choice. Please try again.")
