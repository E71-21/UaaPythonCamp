import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("320x500")
root.title("Calculator by Eli")

anwser = tk.IntVar(value=0)

def calculate(equation):
    print(equation)
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
    print(equation)
    new_first_value = equation[0]
    print(new_first_value)
    current_equation.clear()
    current_equation_str = ""
    current_equation.append(new_first_value)
    current_equation.append(" ")
    current_equation.append("")
    current_equation_str = str(new_first_value)
    print(current_equation)
    print(current_equation_str)
    print(equation)

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
    print(current_equation_str.split("+"))
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
    current_equation[0] = int(float(split_equation[0])) if current_equation != None else current_equation[0]
    current_equation[1] = operation
    try:
        current_equation[2] = int(split_equation[1])
    except:
        pass
    print(current_equation)
    anwser.set(current_equation_str)

def number_button_clicked(value):
    global current_equation_str
    current_equation_str = current_equation_str + str(value)
    anwser.set(value)
    check_equation()

def operation_button_clicked(value):
    global current_equation_str
    current_equation_str = current_equation_str + str(value)
    anwser.set(value)
    check_equation()

result_display = tk.Label(root, textvariable=anwser, font=("Times New Roman", 30)).pack(side=tk.TOP)

current_equation_str = ""
current_equation = ["", "", ""]

button1 = ttk.Button(root, text="1", command=lambda value=1: number_button_clicked(value))
button2 = ttk.Button(root, text="2", command=lambda value=2: number_button_clicked(value))
button3 = ttk.Button(root, text="3", command=lambda value=3: number_button_clicked(value))
button4 = ttk.Button(root, text="4", command=lambda value=4: number_button_clicked(value))
button5 = ttk.Button(root, text="5", command=lambda value=5: number_button_clicked(value))
button6 = ttk.Button(root, text="6", command=lambda value=6: number_button_clicked(value))
button7 = ttk.Button(root, text="7", command=lambda value=7: number_button_clicked(value))
button8 = ttk.Button(root, text="8", command=lambda value=8: number_button_clicked(value))
button9 = ttk.Button(root, text="9", command=lambda value=9: number_button_clicked(value))
button0 = ttk.Button(root, text="0", command=lambda value=0: number_button_clicked(value))

button1.pack()
button2.pack()
button3.pack()
button4.pack()
button5.pack()
button6.pack()
button7.pack()
button8.pack()
button9.pack()
button0.pack()

add_button = ttk.Button(root, text="+", command=lambda value="+": operation_button_clicked(value))
subtract_button = ttk.Button(root, text="-", command=lambda value="-": operation_button_clicked(value))
multiply_button = ttk.Button(root, text="*", command=lambda value="*": operation_button_clicked(value))
divide_button = ttk.Button(root, text="/", command=lambda value="/": operation_button_clicked(value))
calculate_button = ttk.Button(root, text="=", command=lambda equation=current_equation: calculate(equation))

add_button.pack()
subtract_button.pack()
multiply_button.pack()
divide_button.pack()
calculate_button.pack()

root.mainloop()