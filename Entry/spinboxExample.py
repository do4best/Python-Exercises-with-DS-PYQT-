from tkinter import *
root = Tk()
root.geometry('500x500')
al = StringVar()
def display():
    root.configure(bg=al.get())

mys1 = Spinbox(font=('Calibri',15),command=display,values=['Red','Green','Blue','Violet','Indigo','Magenta','Yellow'],textvariable=al)
mys1.pack()
root.mainloop()