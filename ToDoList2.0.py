import tkinter as tk
from tkinter import messagebox

Tasks = []

def add_task():
    task = entry_task.get()
    if task == "":
        messagebox.showwarning("Input Error", "Task cannot be empty!")
    elif task.isdigit():
        messagebox.showwarning("Input Error", "Task must be a string, not a number!")
    elif not task.isalnum():
        messagebox.showwarning("Input Error", "Task must be a string, not signs!")
    else:
        Tasks.append(task)
        update_task_list()
        entry_task.delete(0, tk.END)

def view_tasks():
    if len(Tasks) == 0:
        messagebox.showinfo("No Tasks", "You have no tasks available.")
    else:
        update_task_list()

def task_completed():
    try:
        task_number = int(entry_task.get()) - 1
        if 0 <= task_number < len(Tasks):
            Tasks[task_number] = f"[X] {Tasks[task_number]}"
            update_task_list()
        else:
            messagebox.showwarning("Invalid Task", "Please enter a valid task number.")
    except ValueError:
        messagebox.showwarning("Input Error", "Please enter a valid task number.")

def delete_task():
    try:
        task_number = int(entry_task.get()) - 1
        if 0 <= task_number < len(Tasks):
            del Tasks[task_number]
            update_task_list()
        else:
            messagebox.showwarning("Invalid Task", "Please enter a valid task number.")
    except ValueError:
        messagebox.showwarning("Input Error", "Please enter a valid task number.")

def update_task_list():
    task_listbox.delete(0, tk.END)
    for idx, task in enumerate(Tasks, start=1):
        task_listbox.insert(tk.END, f"{idx}. {task}")

def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in Tasks:
            file.write(task + "\n")
    messagebox.showinfo("Saved", "Tasks saved successfully!")

def Exit():
    if messagebox.askyesno("Exit", "Do you want to exit the application?"):
        root.destroy()
        with open("tasks.txt", "w") as file:
            for task in Tasks:
                file.write(task + "\n")
                exit()
            else:
                root.destroy()

root = tk.Tk()
root.title("To-Do List Application")

label = tk.Label(root, text="To-Do List", font=("Arial", 16))
label.pack(pady=10)

entry_task = tk.Entry(root, width=30)
entry_task.pack(pady=10)

add_button = tk.Button(root, text="Add Task", width=20, command=add_task)
add_button.pack(pady=5)

view_button = tk.Button(root, text="View Tasks", width=20, command=view_tasks)
view_button.pack(pady=5)

complete_button = tk.Button(root, text="Mark as Completed", width=20, command=task_completed)
complete_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", width=20, command=delete_task)
delete_button.pack(pady=5)

save_button = tk.Button(root, text="Save Tasks", width=20, command=save_tasks)
save_button.pack(pady=5)

exit_button = tk.Button(root, text="Exit", width=20, command=Exit)
exit_button.pack(pady=5)

task_listbox = tk.Listbox(root, width=50, height=10)
task_listbox.pack(pady=10)

root.mainloop()
