todo = []
print('Welcome!')
c = 1
while c:
    print("Enter operation:\n1. Add\n2. Edit\n3. Delete")
    act = int(input("Your choice: "))
    if act == 1:
        task = input("Enter the task to add: ")
        todo.append(task)
    elif act == 2:
        oldtask = input("Enter the task to edit: ")
        if oldtask in todo:
            newtask = input("Enter the new task: ")
            index = todo.index(oldtask)
            todo[index] = newtask
        else:
            print("Task not found.")
    elif act == 3:
        task = input("Enter the task to delete: ")
        if task in todo:
            todo.remove(task)
        else:
            print("Task not found.")
    else:
        print("Invalid choice.")
    print("Current To-Do List:", todo)
    c = int(input("Continue? (1 for yes, 0 for no): "))

