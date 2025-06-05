import tkinter as tk
from tkinter import ttk
from tkinter import font as tkFont

root = tk.Tk()
root.geometry("350x280")
root.title("Calculator by Eli")

helv36 = tkFont.Font(family='Helvetica', size = 50, weight="bold")

anwser = tk.IntVar(value=0)

def calculate(equation):
    # print(str(equation) + "Calculate")
    global anwser
    global current_equation
    global current_equation_str
    value1 = equation[0]
    value2 = equation[2]
    operation = equation[1]
    if operation == "+":
        anwser.set(round(add(value1, value2), 10))
        del equation[0]
        del equation[0]
        equation[0] = round(add(value1, value2), 10)
    elif operation == "-":
        anwser.set(round(subtract(value1, value2), 10))
        del equation[0]
        del equation[0]
        equation[0] = round(subtract(value1, value2), 10)
    elif operation == "*":
        anwser.set(round(multiply(value1, value2), 10))
        del equation[0]
        del equation[0]
        equation[0] = round(multiply(value1, value2), 10)
    elif operation == "/":
        anwser.set(round(divide(value1, value2), 10))
        del equation[0]
        del equation[0]
        equation[0] = round(divide(value1, value2), 10)
    # print(equation)
    new_first_value = equation[0]
    # print(new_first_value)
    current_equation.clear()
    current_equation_str = ""
    current_equation.append(new_first_value)
    current_equation.append(" ")
    current_equation.append("")
    current_equation_str = str(new_first_value)
    # print(current_equation)
    # print(current_equation_str)
    # print(equation)

def subtract(value1, value2):
    return value1-value2

def add(value1, value2):
    return value1+value2

def divide(value1, value2):
    return value1/value2

def multiply(value1, value2):
    return value1*value2

def check_equation():
    global current_equation
    global current_equation_str
    global anwser
    operation = " "
    if "+" in current_equation_str:
        operation = "+"
    if "-" in current_equation_str:
        operation = "-"
    if "*" in current_equation_str:
        operation = "*"
    if "/" in current_equation_str:
        operation = "/"
    split_equation = current_equation_str.split(str(operation))
    current_equation[0] = float(split_equation[0]) if current_equation != None else current_equation[0]
    current_equation[1] = operation
    try:
        current_equation[2] = float(split_equation[1])
    except:
        pass
    # print(current_equation)
    # print(current_equation_str)
    anwser.set(current_equation_str)

def number_button_clicked(value):
    global current_equation_str
    global anwser
    current_equation_str = current_equation_str + str(value)
    anwser.set(value)
    check_equation()

def operation_button_clicked(value):
    global current_equation_str
    global anwser
    current_equation_str = current_equation_str + str(value)
    anwser.set(value)
    check_equation()

def clear():
    global current_equation
    global current_equation_str
    global anwser
    current_equation = ["", " ", ""]
    current_equation_str = ""
    # print(current_equation)
    # print(current_equation_str)
    anwser.set(0)

frame1 = tk.Frame(root)
frame1.grid(row=0, column=0, padx=(20,20), pady=(10,10))

result_display = tk.Label(frame1, textvariable=anwser, font=("Times New Roman", 30)).grid(row=0, column=2, pady=10)
current_equation_str = ""
current_equation = ["", "", ""]

frame2 = tk.Frame(root)
frame2.grid(row=1, column=0, padx=(20,20), pady=(10,10))

button1 = ttk.Button(frame2, text="1", command=lambda value=1: number_button_clicked(value))
button2 = ttk.Button(frame2, text="2", command=lambda value=2: number_button_clicked(value))
button3 = ttk.Button(frame2, text="3", command=lambda value=3: number_button_clicked(value))
button4 = ttk.Button(frame2, text="4", command=lambda value=4: number_button_clicked(value))
button5 = ttk.Button(frame2, text="5", command=lambda value=5: number_button_clicked(value))
button6 = ttk.Button(frame2, text="6", command=lambda value=6: number_button_clicked(value))
button7 = ttk.Button(frame2, text="7", command=lambda value=7: number_button_clicked(value))
button8 = ttk.Button(frame2, text="8", command=lambda value=8: number_button_clicked(value))
button9 = ttk.Button(frame2, text="9", command=lambda value=9: number_button_clicked(value))
button0 = ttk.Button(frame2, text="0", command=lambda value=0: number_button_clicked(value))


button1.grid(row=1, column=0, padx=2, pady=2)
button2.grid(row=1, column=1, padx=2, pady=2)
button3.grid(row=1, column=2, padx=2, pady=2)
button4.grid(row=2, column=0, padx=2, pady=2)
button5.grid(row=2, column=1, padx=2, pady=2)
button6.grid(row=2, column=2, padx=2, pady=2)
button7.grid(row=3, column=0, padx=2, pady=2)
button8.grid(row=3, column=1, padx=2, pady=2)
button9.grid(row=3, column=2, padx=2, pady=2)
button0.grid(row=4, column=1, padx=2, pady=2)

add_button = ttk.Button(frame2, text="+", command=lambda value="+": operation_button_clicked(value))
subtract_button = ttk.Button(frame2, text="-", command=lambda value="-": operation_button_clicked(value))
multiply_button = ttk.Button(frame2, text="*", command=lambda value="*": operation_button_clicked(value))
divide_button = ttk.Button(frame2, text="/", command=lambda value="/": operation_button_clicked(value))
calculate_button = ttk.Button(frame2, text="=", command=lambda: calculate(current_equation))

clear_buttom = ttk.Button(frame2, text="Clear", command=clear)
clear_buttom.grid(row=4, column=0, padx=2, pady=2)

add_button.grid(row=1, column=3, padx=2, pady=2)
subtract_button.grid(row=2, column=3, padx=2, pady=2)
multiply_button.grid(row=3, column=3, padx=2, pady=2)
divide_button.grid(row=4, column=3, padx=2, pady=2)
calculate_button.grid(row=4, column=2, padx=2, pady=2)

root.mainloop()