import tkinter as tk
import random
from time import sleep

colors = ["RED", "BLUE", "GREEN", "YELLOW", "PURPLE", "PINK", "ORANGE"]

window = tk.Tk()
window.title("ELI!!!")

canvases = []

for i in range(15):
    color = random.choice(colors)
    canvas = tk.Canvas(master=window, background=color, height=50, width=50).pack()
    canvases.append(canvas)



window.mainloop()

