import firebase_admin, sys
from tkinter import *
from tkinter.ttk import *


if __name__=="__main__":
    root = Tk()
    f1 = Frame(root)
    f1.pack()
    button = Button(f1, text='I am your first button')
    button.pack()
    root.title("Firt_program")
    label = Label(root, text="Hello World!").pack()
    root.mainloop(0)