Tasks = []
def add_task(): #1
    task = input("Enter a task: ")
    if task.isdigit():
        print("Task must be a string")
    elif task == "":
        print("Task cannot be empty")
    else:
        Tasks.append(task)
        print("Task added successfully!")

def view_tasks(): #2
    if len(Tasks) == 0:
        print("No tasks available")
    else:
        print("Your tasks:")
        for i in range(len(Tasks)):
            print(f"{i+1}. {Tasks[i]}")

def task_completed(): #3
    view_tasks()
    task_number = int(input("Enter the task number you want to mark as completed: "))
    if task_number > 0 and task_number <= len(Tasks):
        Tasks[task_number - 1] = f"[X] {Tasks[task_number -1]}"
        print("Task marked as completed!")
    else:
        print("Invalid task number")

def delete_task(): #4
    view_tasks()
    task_number = int(input("Enter the task number you want to delete: "))
    if task_number > 0 and task_number <= len(Tasks):
        del Tasks[task_number - 1]
        print("Task deleted successfully!")
    else:
        print("Invalid task number")

def save_tasks(): #5
    with open("tasks.txt", "w") as file:
        for task in Tasks:
            file.write(task + "\n")
        print("Tasks saved successfully!")

def Exit(): #6
    save_tasks()
    print("Exiting...")
    exit()
        

print("Welcome to your to-do list application!")
print("Choose action please:")
print('1. Add task')
print('2. View tasks')
print('3. Mark task as completed')
print('4. Delete task')
print('5. Save tasks')
print('6. Exit')



while True:
    choice = input("Enter your choice: ")
    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        task_completed()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        save_tasks()
    elif choice == '6':
        Exit()
    else:
        print("Invalid choice. Please choose a valid option.")
