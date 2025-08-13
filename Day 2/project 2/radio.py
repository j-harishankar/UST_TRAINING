import tkinter as tk
from tkinter import ttk, messagebox
import os
import csv








txt_file = "Paliendrome.txt"
csv_file = "ReversedTable.csv"

root = tk.Tk()
root.geometry("440x400")
root.title('Palindrome Check')
root.resizable(True, True)


if not os.path.exists(txt_file):
    with open(txt_file, 'w', newline="") as fp:
        fp.write("PALIENDROME LIST\n===================\n")

if not os.path.exists(csv_file):
    with open(csv_file, 'w', newline='') as fp:
        writer = csv.writer(fp)
        writer.writerow(['Given', 'Reversed'])



def verify_user_entry(event):
    reverse_label.config(text="")
    if not event.char.isalnum():
        given_string_Entry.delete(0,tk.END)
        given_string_Entry.insert(0,given_string_Entry.get()[:-1])
privilege = tk.IntVar()




pal_label = ttk.Label(root, text="PALIENDROME CHECK")
pal_label.grid(column=0, row=0, columnspan=2, pady=10)

admin_rdo_btn = ttk.Radiobutton(root, text="ADMINISTRATOR", variable=privilege, value=1)
admin_rdo_btn.grid(column=0, row=1, sticky=tk.W, padx=20, pady=5)

user_rdo_btn = ttk.Radiobutton(root, text="USER", variable=privilege, value=0)
user_rdo_btn.grid(column=1, row=1, sticky=tk.W, padx=20, pady=5)

given_string_label = ttk.Label(root, text="Given String")
given_string_label.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)

given_string_Entry = ttk.Entry(root)
given_string_Entry.grid(column=1, row=2, sticky=tk.W, padx=5, pady=5)
given_string_Entry.bind('<KeyRelease>', verify_user_entry)

reverse_btn = ttk.Button(root,text="Reverse")
reverse_btn.grid(column=2, row=2, sticky=tk.W, padx=5, pady=5)


reverse_label = ttk.Label(root,text="Reversed String:")
reverse_label.grid(column=0, row=3, sticky=tk.W, padx=10, pady=10)



reverse_label = ttk.Label(root,text="",font='Helvetica 12 bold')
reverse_label.grid(column=1, row=3, sticky=tk.W, padx=5, pady=5)


root.mainloop()
