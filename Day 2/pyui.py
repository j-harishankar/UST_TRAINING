import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
root = tk.Tk()
root.geometry("440x400")
root.title('Palindrome Check')
root.resizable(True, True)

def show_reverse():
    given_str = given_string_Entry.get()
    if len(given_str) != 0:
        result_str = given_str[::-1]
        reverse_label.config(text =  result_str)
    else:
        messagebox.showwarning("Empty","Input is mandatory")
    if given_str == result_str:
        messagebox.showinfo(result_str,"paliendrome")
    else:
        messagebox.showinfo(result_str,"Not a Palienrome")
pal_label = ttk.Label(root, text="PALINDROME CHECK")
pal_label.grid(column=0, row=0, sticky=tk.W, padx=20, pady=20, columnspan=2)

given_string_label = ttk.Label(root, text="Given String")
given_string_label.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)

given_string_Entry = ttk.Entry(root)
given_string_Entry.grid(column=1, row=2, sticky=tk.W, padx=5, pady=5)


reverse_btn = ttk.Button(root,text="Reverse",command = show_reverse)
reverse_btn.grid(column=2, row=2, sticky=tk.W, padx=5, pady=5)


reverse_label = ttk.Label(root,text="Reversed String:")
reverse_label.grid(column=0, row=3, sticky=tk.W, padx=10, pady=10)



reverse_label = ttk.Label(root,text="",font='Helvetica 12 bold')
reverse_label.grid(column=1, row=3, sticky=tk.W, padx=5, pady=5)




root.mainloop()
