import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import filedialog

def load():
    file_path = filedialog.askopenfile().name
    file_text = open(file_path, "r").read()
    text_area.delete('1.0', tk.END)
    text_area.insert(tk.END, file_text)

def save():
    file_path = filedialog.asksaveasfile().name
    open(file_path, "w").write(text_area.get("1.0", tk.END))

root = tk.Tk()
root.geometry("800x500")
root.title("Text Edit by Eli")

text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=8, font=("Times New Roman", 15))
text_area.pack(expand=True, fill="both")

load_button = ttk.Button(text="Load", command=load).pack(side=tk.LEFT, pady=2)
save_button = ttk.Button(text="Save", command=save).pack(side=tk.LEFT)

text_area.focus()
root.mainloop()