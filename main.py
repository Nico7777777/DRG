import firebase_admin, sys
from tkinter import *
from tkinter.ttk import *


if __name__=="__main__":
    root = Tk("Medfy")
    f1 = Frame(root)
    f1.pack()
    screen_height = root.winfo_screenheight()
    screen_width = root.winfo_screenwidth()
    root.geometry(f'{screen_width}x{screen_height}')
    button = Button(f1, text='I am your first button')
    button.pack()
    root.title("Medfy pentru Guvernul Romaniei")
    try:
        from ctypes import windll
        windll.shcore.setProcessDpiAwareness(1)
    finally:
        root.mainloop(0)