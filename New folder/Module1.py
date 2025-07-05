from tkinter import *
top = Tk()
top.title("main")
top.geometry('300x300')

n1=Label(top,text="Name").grid(row=0,column=0)
e1=Entry(top).grid(row=0,column=1)

n1=Label(top,text="Email").grid(row=0,column=2)
e1=Entry(top).grid(row=0,column=3)

n1=Label(top,text="Address").grid(row=1,column=0)
e1=Entry(top).grid(row=1,column=1)

n1=Label(top,text="conract").grid(row=1,column=2)
e1=Entry(top).grid(row=1,column=3)

btn=Button(top,text="Save").grid(row=2,column=0)
