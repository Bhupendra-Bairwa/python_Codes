from tkinter import *

top1=Tk()

top1.title("main")
top1.geometry('300x300')

def cust():
    import Abc
    top1.destroy()

n1=Label(top1,text="Name").grid(row=0,column=0)

e1=Entry(top1).grid(row=0,column=1)


n1=Label(top1,text="Address").grid(row=1,column=0)

e1=Entry(top1).grid(row=1,column=1)

btn=Button(top1,text="Save", command=cust).grid(row=2,column=0)

