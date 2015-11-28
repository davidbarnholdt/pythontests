from tkinter import *

root = Tk()

def printName():
    print("Hello my name is asdf")

def printName2(event):
    print("Hello my name is 123123")

label_1 = Label(root, text="Name")
label_2 = Label(root, text="Password yes")
entry_1 = Entry(root)
entry_2 = Entry(root)


label_1.grid(row=0, sticky=W)
label_2.grid(row=1, sticky=W)

entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)

c = Checkbutton(root, text="Keep me signed in")
c.grid(columnspan=2)

button_1 = Button(root,text="print my name", command=printName)
button_1.grid(row=3)

button_2 = Button(root,text="print my name2", command=printName)
button_2.bind("<Button-2>", printName2)
button_2.grid(row=4)

root.mainloop()