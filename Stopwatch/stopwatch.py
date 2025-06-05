import tkinter as tk
from tkinter import ttk
from time import sleep

root = tk.Tk()
root.geometry("300x200")
root.title("Stopwatch by Eli")

time_elapsed_formatted = tk.StringVar(value="")

seconds_elapsed = 0
paused = True
def start():
    global seconds_elapsed
    global paused
    paused = False
    while not paused:
        sleep(1)
        seconds_elapsed += 1
        time_elapsed_formatted.set(str(seconds_elapsed//3600) + ":" + str((seconds_elapsed%3600)//60) + ":" + str((seconds_elapsed%3600)%60))
        time_label.update()
        print(str(seconds_elapsed//3600) + ":" + str((seconds_elapsed%3600)//60) + ":" + str((seconds_elapsed%3600)%60))

def pause():
    global paused
    paused = True
    print("Paused")

def reset():
    global paused
    global seconds_elapsed
    paused = True
    seconds_elapsed = 0
    time_elapsed_formatted.set(str(seconds_elapsed//3600) + ":" + str((seconds_elapsed%3600)//60) + ":" + str((seconds_elapsed%3600)%60))
    time_label.update()


frame1 = tk.Frame(root)
frame1.grid(row=0, column=0, padx=30, pady=20)

start_button = ttk.Button(frame1, text="Start", command=start)
pause_button = ttk.Button(frame1, text="Pause", command=pause)
reset_button = ttk.Button(frame1, text="Reset", command=reset)

start_button.grid(row=0, column=0)
pause_button.grid(row=0, column=1)
reset_button.grid(row=0, column=2)

frame2 = tk.Frame(root)
frame2.grid(row=1, column=0)

time_label = ttk.Label(frame2, textvariable=time_elapsed_formatted, font=("Times New Roman", 50))
time_label.grid(row=0, column=2)


root.mainloop()