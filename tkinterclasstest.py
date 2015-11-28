from tkinter import *



class SpelPlan:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.printButton = Button(frame,text="Print message", command=self.printMessage)

