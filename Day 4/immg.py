import tkinter as tk
from tkinter.ttk import Frame
from tkinter import (PhotoImage)

class Ust(Frame):
    def __init__(self,master):
        super().__init__(master,relief='flat',borderwidth=40)
        self.master.title("UST to Marian")
        self.pack(fill=None,expand=0)
        self.photo = PhotoImage(file='Ust.png')
        btn= tk.Button(self, text="test",image=self.photo,command=self.to_marian)
        btn.pack()
    def to_marian(self):
        Marian(self.master,self).show()

class Marian(Frame):
    def __init__(self,parent,main_page):
        super().__init__(parent)
        self.top= tk.Toplevel(parent,relief='flat',borderwidth=40)
        self.main_page = main_page
        self.pack(fill=None, expand=0)
        self.photo = PhotoImage(file='MARIAN.png')
        button = tk.Button(self.top, image=self.photo, command=self.to_ust)
        button.grid()
    def to_ust(self):
        self.top.destroy()
        self.destroy()

def main():
    root = tk.Tk()
    root.geometry("800x800")
    root.resizable(True, True)
    Ust(root)
    root.mainloop()

main()