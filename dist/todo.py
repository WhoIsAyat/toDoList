import tkinter as tk
from tkinter import messagebox
import os
from datetime import datetime

# File name for storing tasks
TASKS_FILE = "tasks.txt"

# Function to add a task with a timestamp
def add_task():
    task = entry.get()
    if task:
        time_added = datetime.now().strftime("%H:%M")  # Get current time in "HH:MM" format
        task_with_time = f"{task} (Added at {time_added})"
        listbox.insert(tk.END, task_with_time)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

# Function to delete the selected task
def delete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

# Function to save tasks to a file
def save_tasks():
    tasks = listbox.get(0, tk.END)
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Function to load tasks from a file
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            tasks = file.readlines()
            for task in tasks:
                listbox.insert(tk.END, task.strip())

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Configure window style
root.configure(bg="#e0e0e0")  # Window background color

# Task input field
entry = tk.Entry(root, width=35, font=("Arial", 14))
entry.pack(pady=10)

# Add task button
add_button = tk.Button(root, text="Add Task", command=add_task, 
                       bg="black", fg="white", font=("Arial", 12))
add_button.pack(pady=5)

# Delete task button
delete_button = tk.Button(root, text="Delete Task", command=delete_task, 
                          bg="black", fg="white", font=("Arial", 12))
delete_button.pack(pady=5)

# Task list
listbox = tk.Listbox(root, width=45, height=10, font=("Arial", 12), selectmode=tk.SINGLE)
listbox.pack(pady=10)

# Load tasks on startup
load_tasks()

# Save tasks on window close
root.protocol("WM_DELETE_WINDOW", lambda: (save_tasks(), root.destroy()))

# Run the main loop
root.mainloop()
