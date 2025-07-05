from tkinter import *
top = Tk()
top.title("main")
top.geometry('300x300')

def Msd():
    import Module1
    top.destroy()

n1=Label(top,text="Name").grid(row=0,column=0)
e1=Entry(top).grid(row=1,column=0)

n1=Label(top,text="Email").grid(row=2,column=0)
e1=Entry(top).grid(row=3,column=0)

n1=Label(top,text="Address").grid(row=4,column=0)
e1=Entry(top).grid(row=5,column=0)

n1=Label(top,text="conract").grid(row=6,column=0)
e1=Entry(top).grid(row=7,column=0)

btn=Button(top,text="Save",command=Msd).grid(row=8,column=0)
