import tkinter as tk
from tkinter import ttk
from time import sleep


root = tk.Tk()
root.geometry("400x200")
root.title("Timer by Eli")

time_left = 0

display_time_left = tk.StringVar(value="")

def start_timer():
    global time_left
    hours = int(hour_select.get())
    minutes = int(minute_select.get())
    seconds = int(seconds_select.get())
    print(hours, minutes, seconds)

    seconds += minutes*60
    seconds += hours*60*60
    print(seconds)
    time_left = seconds
    time_left_label.update()

    for i in range(seconds):
        sleep(1)
        if time_left == 0:
            display_time_left.set("")
            break
        seconds_left = time_left
        seconds_left -= 1
        time_left_formatted = str(seconds_left//(60*60)) + ":" + str((seconds_left%(60*60)//60)) + ":" + str((seconds_left%(60*60)%60))
        print(time_left_formatted)
        display_time_left.set(time_left_formatted)
        time_left = seconds_left
        time_left_label.update()

def cancel_timer():
    global time_left
    time_left = 0

frame1 = tk.Frame(root).grid(row=0, column=0)

hour_label = ttk.Label(frame1, text="Hours: ")

hour_select = tk.Spinbox(frame1, from_=0, to=1000000, width=10, repeatdelay=500, repeatinterval=100)
hour_select.config(state="normal", cursor="hand2", bd=3, justify="center", wrap=True)

hour_label.grid(row=0, column=0)
hour_select.grid(row=0, column=1)

minute_label = ttk.Label(frame1, text="Minutes: ")

minute_select = tk.Spinbox(frame1, from_=0, to=59, width=10, repeatdelay=500, repeatinterval=100)
minute_select.config(state="normal", cursor="hand2", bd=3, justify="center", wrap=True)

minute_label.grid(row=1, column=0)
minute_select.grid(row=1, column=1)

seconds_label = ttk.Label(frame1, text="Seconds: ")

seconds_select = tk.Spinbox(frame1, from_=0, to=59, width=10, repeatdelay=500, repeatinterval=100)
seconds_select.config(state="normal", cursor="hand2", bd=3, justify="center", wrap=True)

seconds_label.grid(row=2, column=0)
seconds_select.grid(row=2, column=1)

start_timer_button = ttk.Button(frame1, text="Start Timer", command=start_timer)
start_timer_button.grid(row=1, column=2, padx=50)

cancel_timer_button = ttk.Button(frame1, text="Cancel Timer", command=cancel_timer)
cancel_timer_button.grid(row=2, column=2, padx=50)

frame2 = tk.Frame(root).grid(row=1, column=0)

time_left_label = ttk.Label(root, textvariable=display_time_left, font=("Times New Roman", 50))
time_left_label.grid(row=3, column=1, columnspan=5)

root.mainloop()