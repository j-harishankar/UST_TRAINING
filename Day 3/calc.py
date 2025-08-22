import tkinter as tk
from tkinter import ttk, messagebox

root = tk.Tk()
root.geometry("440x300")
root.title('Simple Calculator')
root.resizable(True, True)

def get_numbers():
    """Retrieve numbers from entry fields and handle invalid input."""
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        return num1, num2
    except ValueError:
        messagebox.showwarning("Invalid Input", "Please enter valid numbers")
        return None, None

def add():
    num1, num2 = get_numbers()
    if num1 is not None:
        result_label.config(text=str(num1 + num2))

def subtract():
    num1, num2 = get_numbers()
    if num1 is not None:
        result_label.config(text=str(num1 - num2))

def multiply():
    num1, num2 = get_numbers()
    if num1 is not None:
        result_label.config(text=str(num1 * num2))

def divide():
    num1, num2 = get_numbers()
    if num1 is not None:
        if num2 == 0:
            messagebox.showerror("Error", "Division by zero not allowed")
            return
        result_label.config(text=str(num1 / num2))

title_label = ttk.Label(root, text="SIMPLE CALCULATOR", font=("Helvetica", 14, "bold"))
title_label.grid(column=0, row=0, columnspan=4, pady=10)


label_num1 = ttk.Label(root, text="First Number:")
label_num1.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
entry_num1 = ttk.Entry(root)
entry_num1.grid(column=1, row=1, sticky=tk.W, padx=5, pady=5)


label_num2 = ttk.Label(root, text="Second Number:")
label_num2.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)
entry_num2 = ttk.Entry(root)
entry_num2.grid(column=1, row=2, sticky=tk.W, padx=5, pady=5)

ttk.Button(root, text="+", command=add).grid(column=0, row=3, padx=5, pady=5)
ttk.Button(root, text="-", command=subtract).grid(column=1, row=3, padx=5, pady=5)
ttk.Button(root, text="*", command=multiply).grid(column=2, row=3, padx=5, pady=5)
ttk.Button(root, text="/", command=divide).grid(column=3, row=3, padx=5, pady=5)


ttk.Label(root, text="Result:", font=("Helvetica", 12)).grid(column=0, row=4, sticky=tk.W, padx=5, pady=10)
result_label = ttk.Label(root, text="", font=("Helvetica", 12, "bold"))
result_label.grid(column=1, row=4, sticky=tk.W, padx=5, pady=10)

root.mainloop()
