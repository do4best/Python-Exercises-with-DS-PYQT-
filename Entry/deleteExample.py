from tkinter import *
from tkinter import ttk
class MyDeleteExample(Tk):

    def __init__(self):
        super().__init__()

        self.title('Delete Example')
        self.geometry('500x500')
        self.myel = Entry(self,font=('Arial', 14),width=34,bd=5)
        self.myel.pack(side=LEFT)

        self.button1 = Button(self,text="Delete the Text",command=lambda: fuck(self,self.myel))
        self.button1.pack(pady=32)

        def fuck(self,myel):
            myel.delete(first=0, last=15)

if __name__ == '__main__':
    app = MyDeleteExample()
    app.mainloop()
    print('Done')