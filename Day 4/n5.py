import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('440x300')
root.title("Largest Number")
root.resizable(0,0)

largest_among_two=tk.BooleanVar()
largest_among_two.set(False)
largest_among_three=tk.BooleanVar()
largest_among_three.set(False)

def largest_among_two_changed():
    val=largest_among_two.get()
    if not val:
        l2_number1_entry.config(state=tk.DISABLED)
        l2_number2_entry.config(state=tk.DISABLED)
    else:
        l2_number1_entry.config(state=tk.NORMAL)
        l2_number2_entry.config(state=tk.NORMAL)
def largest_among_three_changed():
    val=largest_among_three.get()
    if not val:
        l3_number1_entry.config(state=tk.DISABLED)
        l3_number2_entry.config(state=tk.DISABLED)
        l3_number3_entry.config(state=tk.DISABLED)
    else:
        l3_number1_entry.config(state=tk.NORMAL)
        l3_number2_entry.config(state=tk.NORMAL)
        l3_number3_entry.config(state=tk.NORMAL)

l2_chk_bn = ttk.Checkbutton(root, text="Largest Among Two Numbers",
                             command=largest_among_two_changed,
                             variable=largest_among_two)
l2_chk_bn.grid(column=0, row=0,sticky=tk.W,padx=5,pady=5,columnspan=2)

l3_chk_bn=ttk.Checkbutton(root, text="Largest Among Three Numbers",
                          command=largest_among_three_changed,
                          variable=largest_among_three)
l3_chk_bn.grid(column=2, row=0,sticky=tk.W,padx=5,pady=5,columnspan=2)

l2_number1_label = ttk.Label(root, text="Number1")
l2_number1_label.grid(column=0, row=1, sticky=tk.W, padx=20, pady=5)

l2_number1_entry = ttk.Entry(root, state='disabled')
l2_number1_entry.grid(column=1, row=1, sticky=tk.W, padx=5, pady=5)

l2_number2_label = ttk.Label(root, text="Number2")
l2_number2_label.grid(column=0, row=2, sticky=tk.W, padx=20, pady=5)

l2_number2_entry = ttk.Entry(root, state='disabled')
l2_number2_entry.grid(column=1, row=2, sticky=tk.W, padx=5, pady=5)


l3_number1_label = ttk.Label(root, text="Number1")
l3_number1_label.grid(column=2, row=1, sticky=tk.W, padx=5, pady=5)

l3_number1_entry = ttk.Entry(root, state='disabled')
l3_number1_entry.grid(column=3, row=1, padx=5, pady=5)

l3_number2_label = ttk.Label(root, text="Number2")
l3_number2_label.grid(column=2, row=2, sticky=tk.W, padx=5, pady=5)

l3_number2_entry = ttk.Entry(root, state='disabled')
l3_number2_entry.grid(column=3, row=2, padx=5, pady=5)

l3_number3_label = ttk.Label(root, text="Number3")
l3_number3_label.grid(column=2, row=3, sticky=tk.W, padx=5, pady=5)

l3_number3_entry = ttk.Entry(root, state='disabled')
l3_number3_entry.grid(column=3, row=3, padx=5, pady=5)


root.mainloop()