import tkinter as tk
from tkinter import ttk
import subprocess


root = tk.Tk()
root.geometry("1600x900")
root.title("Apps by Eli")

def open_stopwatch():
    subprocess.run(['python', 'Stopwatch/stopwatch.py'])
    # with open("Stopwatch/stopwatch.py", "r") as code_file:
    #     code = code_file.read()
    #     exec(code)

def open_timer():
    subprocess.run(['python', 'Timer/timer.py'])
    # with open("Timer/timer.py", "r") as code_file:
    #     code = code_file.read()
    #     exec(code)

def open_text_edit():
    subprocess.run(['python', 'TextEdit/textedit.py'])
    # with open("TextEdit/textedit.py", "r") as code_file:
    #     code = code_file.read()
    #     exec(code)

def open_calculator():
    subprocess.run(['python', 'Calculator/calculator.py'])
    # with open("Calculator/calculator.py", "r") as code_file:
    #     code = code_file.read()
    #     exec(code)

stopwatch_button = ttk.Button(root, text="Stopwatch", command=open_stopwatch)
timer_button = ttk.Button(root, text="Timer", command=open_timer)
text_edit_button = ttk.Button(root, text="Text Edit", command=open_text_edit)
calculator_button = ttk.Button(root, text="Calculator", command=open_calculator)

stopwatch_button.pack(padx=500, pady=50, expand=True, fill="both")
timer_button.pack(padx=500, pady=50, expand=True, fill="both")
text_edit_button.pack(padx=500, pady=50, expand=True, fill="both")
calculator_button.pack(padx=500, pady=50, expand=True, fill="both")

# stopwatch_button.grid(column=0, row=0, padx=20, pady=50)
# timer_button.grid(column=1, row=0, padx=20, pady=50)
# text_edit_button.grid(column=2, row=0, padx=20, pady=50)
# calculator_button.grid(column=3, row=0, padx=20, pady=50)

root.mainloop()