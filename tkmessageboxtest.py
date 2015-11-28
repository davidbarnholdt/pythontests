#from tkinter import *
#from tkMessageBox import *
import tkinter as tk
from tkinter import messagebox


top = tk.Tk()
def hello():
    messagebox.showinfo("Say Hello", "Hello World")
    result = messagebox.Dialog()
    result = messagebox.askquestion("Tell me your name")
    messagebox.showinfo("your name is", result)

B1 = tk.Button(top, text = "Say Hello", command = hello)
B1.pack()

top.mainloop()