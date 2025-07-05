from tkinter import *

top=Tk()

top.geometry('300x300')

name=Label(top,text="Name").place(x=30, y=60)
e1=Entry(top).place(x=100, y=60)


name1=Label(top,text="Address").place(x=30, y=120)

e1=Entry(top).place(x=100, y=120)

btn=Button(top,text="save").place(x=30, y=150)
