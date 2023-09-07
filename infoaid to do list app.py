import tkinter as tk
from tkinter import messagebox, filedialog
import json


class Task:
    def __init__(self, title, description, status="Incomplete"):
        self.title = title
        self.description = description
        self.status = status


class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        self.tasks = []

        self.title_label = tk.Label(root, text="Title:")
        self.title_label.pack()

        self.title_entry = tk.Entry(root)
        self.title_entry.pack()

        self.description_label = tk.Label(root, text="Description:")
        self.description_label.pack()

        self.description_entry = tk.Entry(root)
        self.description_entry.pack()

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(pady=5)

        self.save_button = tk.Button(root, text="Save Tasks", command=self.save_tasks)
        self.save_button.pack(pady=5)

        self.load_button = tk.Button(root, text="Load Tasks", command=self.load_tasks)
        self.load_button.pack(pady=5)

        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=10)

    def add_task(self):
        title = self.title_entry.get()
        description = self.description_entry.get()
        if title and description:
            new_task = Task(title, description)
            self.tasks.append(new_task)
            self.task_listbox.insert(tk.END, new_task.title)
            self.title_entry.delete(0, tk.END)
            self.description_entry.delete(0, tk.END)

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            del self.tasks[index]
            self.task_listbox.delete(index)

    def save_tasks(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON Files", "*.json")])
        if file_path:
            with open(file_path, 'w') as file:
                task_data = [{'title': task.title, 'description': task.description, 'status': task.status} for task in
                             self.tasks]
                json.dump(task_data, file)

    def load_tasks(self):
        file_path = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
        if file_path:
            with open(file_path, 'r') as file:
                task_data = json.load(file)
                self.tasks = [Task(task['title'], task['description'], task['status']) for task in task_data]
                self.task_listbox.delete(0, tk.END)
                for task in self.tasks:
                    self.task_listbox.insert(tk.END, task.title)


root = tk.Tk()
app = ToDoListApp(root)
root.mainloop()
