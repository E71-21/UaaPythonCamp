import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import simpledialog
import subprocess
import json

root = tk.Tk()
root.geometry("1600x900")
root.title("Apps by Eli")

with open("apps.json") as file:
        apps = json.load(file)

def add_new_app():
    global apps
    file_path = filedialog.askopenfile().name
    name = simpledialog.askstring("Input", "App Name:")
    apps[name] = {"file_path": file_path, "name": name}
    with open("apps.json", "w") as file:
         json.dump(apps, file, indent=2)
    create_all_buttons()

def create_button(name, filepath, row, collum):
    button = ttk.Button(root, text=name, command=lambda: subprocess.run(['python', filepath]))
    button.grid(row=row, column=collum, padx=50, pady=50, sticky='NSWE')

def create_all_buttons():
    global apps
    for index, app in enumerate(apps.values()):
        root.grid_rowconfigure(index//4, weight=1)
        root.grid_columnconfigure(index%4, weight=1)
        create_button(app["name"], app["file_path"], index//4, index%4)
        if index == len(apps.values()) - 1:
            root.grid_rowconfigure((index+1)//4, weight=1)
            root.grid_columnconfigure((index+1)%4, weight=1)
            button = ttk.Button(root, text="Add New App", command=add_new_app)
            button.grid(row=(index+1)//4, column=(index+1)%4, padx=50, pady=50, sticky='NSWE')


create_all_buttons()
root.mainloop()