import tkinter as tk
from tkinter import ttk,scrolledtext

root = tk.Tk()
root.title("Multiplication Table")
root.geometry("500x400")

def verify_entries(event,entry):
    try:
        int(entry.get())
        reset_btn.configure(state=tk.ACTIVE)
    except ValueError as err:
        print(f'Error: {err}')
        if not event.char.isdigit():
            entry.delete(0, tk.END)
            entry.insert(0, entry.get()[:-1])
            go_btn.configure(state=tk.DISABLED)

def set_or_reset_buttons():
    mt_of_val=mt_of_entry.get()
    mt_till_val=mt_till_entry.get()
    if mt_of_val and mt_till_val:
        go_btn.configure(state=tk.ACTIVE)
        reset_btn.configure(state=tk.ACTIVE)
    else:
        result_label.config(text="")
        go_btn.configure(state=tk.DISABLED)
        reset_btn.configure(state=tk.DISABLED)

def verify_mt_of(event):
    verify_entries(event,mt_of_entry)
    set_or_reset_buttons()
def verify_mt_till(event):
    verify_entries(event,mt_till_entry)
    set_or_reset_buttons()

def show_mt():
    mt_of_val=int(mt_of_entry.get())
    mt_till_val=int(mt_till_entry.get())
    if mt_of_val and mt_till_val:
        result_label.configure(state=tk.ACTIVE)
        #text='Multiplication Table of'+str(mt_of_val)
        text=f"Multiplication Table: {mt_of_val}"
        result_label.config(text=text)

    mt_text=""
    #result_text.delete('0.0',tk.END)
    for i in range(1,mt_till_val+1):
        mt_text+=f"{i}*{mt_of_val}={i*mt_of_val}\n"
    result_text.insert(tk.INSERT,mt_text)
def reset_mt():
    mt_of_entry.delete(0,'end')
    mt_till_entry.delete(0,'end')
    result_label.config(text="")
    result_text.delete('0.0',tk.END)
    go_btn.configure(state=tk.DISABLED)

mt_of_label = ttk.Label(root, text="MT of")
mt_of_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

mt_of_entry = ttk.Entry(root)
mt_of_entry.grid(column=1, row=0, sticky=tk.W, padx=5, pady=5)
mt_of_entry.bind('<KeyRelease>', verify_mt_of)

mt_till_label = ttk.Label(root, text="MT Till")
mt_till_label.grid(column=2, row=0, sticky=tk.W, padx=5, pady=5)

mt_till_entry = ttk.Entry(root)
mt_till_entry.grid(column=3, row=0, sticky=tk.W, padx=5, pady=5)
mt_till_entry.bind('<KeyRelease>', verify_mt_till)

go_btn = ttk.Button(root, text='GO',command=show_mt)
go_btn.grid(column=1, row=1, sticky=tk.W, padx=5, pady=5, columnspan=2)
go_btn['state'] = 'disabled'

result_label = ttk.Label(root, text="", font='Helvetica 12 bold')
result_label.grid(column=1, row=2, sticky=tk.W, padx=5, pady=5, columnspan=3)
result_label['state'] = 'disabled'

result_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=15, height=10)
result_text.grid(column=1, row=3, sticky=tk.W, padx=5, pady=5, columnspan=3)
result_label['state'] = 'disabled'

reset_btn = ttk.Button(root, text='Reset',command=reset_mt)
reset_btn.grid(column=1, row=4, sticky=tk.W, padx=5, pady=5, columnspan=2)
reset_btn['state'] = 'disabled'

root.mainloop()