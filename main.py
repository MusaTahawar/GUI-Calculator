import tkinter as tk
import math

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def clear():
    entry.delete(0, tk.END)

def factorial(num):
    if num < 0:
        return "Error"
    if num == 0:
        return 1
    return math.factorial(num)

def calculate():
    try:
        expression = entry.get()
        expression = expression.replace('^', '**')  # Replace ^ with ** for exponentiation
        expression = expression.replace('!', 'factorial')  # Replace ! with factorial function
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

window = tk.Tk()
window.title("Simple Calculator")

entry = tk.Entry(window, width=20)
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/', "!",
    '4', '5', '6', '*', "^",
    '1', '2', '3', '-', "%",
    '0', '.', '=', '+',
]

row, col = 1, 0
for button_text in buttons:
    if button_text == '=':
        tk.Button(window, text=button_text, command=calculate).grid(row=row, column=col)
    elif button_text == 'C':
        tk.Button(window, text=button_text, command=clear).grid(row=row, column=col)
    else:
        tk.Button(window, text=button_text, command=lambda text=button_text: button_click(text)).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

window.mainloop()
