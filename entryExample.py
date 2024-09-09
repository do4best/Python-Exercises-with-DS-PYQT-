from tkinter import *
class YourState:
    def __init__(self,myroot):
        self.myvar=StringVar()
        self.myvar.set("Hello World")
        self.mylabel=Label(myroot,text="Normal State")
        self.mylabel.grid(row=0,column=0)
        self.mylabel1 = Label(myroot,text="Disable State")
        self.mylabel1.grid(row=1,column=0,pady=10)
        self.mylabel2 = Label(myroot,text="Enable State")
        self.mylabel2.grid(row=2,column=0,pady=10)
        self.entry = Entry(myroot,textvariable=self.myvar,width=15,state='normal')
        self.entry.grid(row=0,column=1,padx=10)
        self.entry1 = Entry(myroot,textvariable=self.myvar,width=15)
        self.entry1.grid(row=1,column=1,padx=10)
        self.entry2 = Entry(myroot,textvariable=self.myvar,width=15,state='disabled')
        self.entry2.grid(row=2,column=1,padx=10)

if __name__ == "__main__":
    root = Tk()
    root.geometry("500x500")
    root.title("Hello World")
    myroot=YourState(root)
    root.mainloop()