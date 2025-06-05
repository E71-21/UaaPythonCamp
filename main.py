import tkinter as tk


buttons_clicked = 0
def on_button_click(row, col):
        global buttons_clicked
        buttons_clicked += 1
        buttons[row][col].configure(text=str(buttons_clicked), background="RED", state=tk.DISABLED)
        
window = tk.Tk()
window.geometry("4000x2500")

buttons = []
for i in range(10):
    row = []
    for j in range(19):
        button = tk.Button(window, text='', width=5, height=2, font=('Helvetica', 20),
                           command=lambda i=i, j=j: on_button_click(i, j))
        button.grid(row=i, column=j, padx=5, pady=5)
        row.append(button)
    buttons.append(row)

window.mainloop()