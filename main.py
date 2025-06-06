import tkinter as tk
from tkinter import ttk
import subprocess


root = tk.Tk()
root.geometry("1600x900")
root.title("Apps by Eli")

def open_stopwatch():
    subprocess.run(['python', 'Stopwatch/stopwatch.py'])

def open_timer():
    subprocess.run(['python', 'Timer/timer.py'])

def open_text_edit():
    subprocess.run(['python', 'TextEdit/textedit.py'])

def open_calculator():
    subprocess.run(['python', 'Calculator/calculator.py'])

def open_tic_tac_toe():
    subprocess.run(['python', 'Tic-Tac-Toe/tic_tac_toe.py'])

def open_crossfire():
    subprocess.run(['python', 'CrossFire/crossfire.py'])

stopwatch_button = ttk.Button(root, text="Stopwatch", command=open_stopwatch)
timer_button = ttk.Button(root, text="Timer", command=open_timer)
text_edit_button = ttk.Button(root, text="Text Edit", command=open_text_edit)
calculator_button = ttk.Button(root, text="Calculator", command=open_calculator)
tic_tac_toe_button = ttk.Button(root, text="Tic-Tac-Toe", command=open_tic_tac_toe)
crossfire_button = ttk.Button(root, text="Cross Fire", command=open_crossfire)

stopwatch_button.pack(padx=500, pady=50, expand=True, fill="both")
timer_button.pack(padx=500, pady=50, expand=True, fill="both")
text_edit_button.pack(padx=500, pady=50, expand=True, fill="both")
calculator_button.pack(padx=500, pady=50, expand=True, fill="both")

tic_tac_toe_button.pack(padx=500, pady=50, expand=True, fill="both")
crossfire_button.pack(padx=500, pady=50, expand=True, fill="both")


# stopwatch_button.grid(column=0, row=0, padx=20, pady=50)
# timer_button.grid(column=1, row=0, padx=20, pady=50)
# text_edit_button.grid(column=2, row=0, padx=20, pady=50)
# calculator_button.grid(column=3, row=0, padx=20, pady=50)

root.mainloop()