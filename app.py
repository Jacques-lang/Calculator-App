import tkinter as tk

calculations = ""


def add_to_calculation(symbol):
    global calculations
    calculations += str(symbol)
    result_and_input_field.delete(1.0, "end")
    result_and_input_field.insert(1.0, calculations)


def evaluate_calculation():
    global calculations
    try:
        calculations = str(eval(calculations))
        result_and_input_field.delete(1.0, "end")
        result_and_input_field.insert(1.0, calculations)
    except:
        clear_field()
        result_and_input_field.delete(1.0, "Error")


def clear_field():
    global calculations
    calculations = ""
    result_and_input_field.delete(1.0, "end")


root = tk.Tk()
root.geometry("300x300")
root.config(background="lightgray")

result_and_input_field = tk.Text(root, height=2, width=16, font=("Arial", 24))
result_and_input_field.grid(columnspan=5)

#buttons
button_1 = tk.Button(root, text="1", command=lambda: add_to_calculation(1), width=5, font=("Arial", 14))
button_1.grid(row=2, column=0)
button_2 = tk.Button(root, text="2", command=lambda: add_to_calculation(2), width=5, font=("Arial", 14))
button_2.grid(row=2, column=1)
button_3 = tk.Button(root, text="3", command=lambda: add_to_calculation(3), width=5, font=("Arial", 14))
button_3.grid(row=2, column=2)
button_4 = tk.Button(root, text="4", command=lambda: add_to_calculation(4), width=5, font=("Arial", 14))
button_4.grid(row=3, column=0)
button_5 = tk.Button(root, text="5", command=lambda: add_to_calculation(5), width=5, font=("Arial", 14))
button_5.grid(row=3, column=1)
button_6 = tk.Button(root, text="6", command=lambda: add_to_calculation(6), width=5, font=("Arial", 14))
button_6.grid(row=3, column=2)
button_7 = tk.Button(root, text="7", command=lambda: add_to_calculation(7), width=5, font=("Arial", 14))
button_7.grid(row=4, column=0)
button_8 = tk.Button(root, text="8", command=lambda: add_to_calculation(8), width=5, font=("Arial", 14))
button_8.grid(row=4, column=1)
button_9 = tk.Button(root, text="9", command=lambda: add_to_calculation(9), width=5, font=("Arial", 14))
button_9.grid(row=4, column=2)
button_0 = tk.Button(root, text="0", command=lambda: add_to_calculation(0), width=5, font=("Arial", 14))
button_0.grid(row=5, column=1)
button_plus = tk.Button(root, text="+", command=lambda :add_to_calculation("+"), width=5, font=("Arial", 14))
button_plus.grid(row=2, column=4)
button_minus = tk.Button(root, text="-", command=lambda :add_to_calculation("-"), width=5, font=("Arial", 14))
button_minus.grid(row=3, column=4)
button_times = tk.Button(root, text="x", command=lambda :add_to_calculation("*"), width=5, font=("Arial", 14))
button_times.grid(row=4, column=4)
button_divide = tk.Button(root, text="/", command=lambda: add_to_calculation("/"), width=5, font=("Arial", 14))
button_divide.grid(row=5, column=4)
button_open = tk.Button(root, text="(", command=lambda: add_to_calculation("("), width=5, font=("Arial", 14))
button_open.grid(row=5, column=0)
button_close = tk.Button(root, text=")", command=lambda: add_to_calculation(")"), width=5, font=("Arial", 14))
button_close.grid(row=5, column=2)
button_clear = tk.Button(root, text="clear", command=clear_field, width=5, font=("Arial", 14))
button_clear.grid(row=6, column=4)
button_equals = tk.Button(root, text="=", command=evaluate_calculation, width=12, font=("Arial", 14))
button_equals.grid(row=6, columnspan=2)


root.mainloop()
