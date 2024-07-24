from tkinter import *

window = Tk()
window.title("Simple Calculator")

num1_label = Label(window, text="Number 1:")
num1_label.grid(row=0, column=0)
num1_entry = Entry(window)
num1_entry.grid(row=0, column=1)

num2_label = Label(window, text="Number 2:")
num2_label.grid(row=1, column=0)
num2_entry = Entry(window)
num2_entry.grid(row=1, column=1)

operation_label = Label(window, text="Operation:")
operation_label.grid(row=2, column=0)
operation_var = StringVar()
operation_var.set("+")  
operation_menu = OptionMenu(window, operation_var, "+", "-", "*", "/")
operation_menu.grid(row=2, column=1)

def perform_calculation():
    try:
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())
        operation = operation_var.get()
        
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Error: Division by zero"
        
        result_label.config(text="Result: " + str(result))
    except ValueError:
        result_label.config(text="Error: Invalid input")

calc_button = Button(window, text="Calculate", command=perform_calculation)
calc_button.grid(row=3, column=0, columnspan=2)

result_label = Label(window, text="Result: ")
result_label.grid(row=4, column=0, columnspan=2)

window.mainloop()