from tkinter import *

win=Tk()
win.geometry('500x500')

name = Label(win,text="Name").place(x=30,y=60)
e1 = Entry(win).place(x=100,y=60)

email = Label(win,text="Email").place(x=30,y=100)
e1 = Entry(win).place(x=100,y=100)

address = Label(win,text="Address").place(x=30,y=140)
e1 = Entry(win).place(x=100,y=140)

contect = Label(win,text="Contect").place(x=30,y=180)
e1 = Entry(win).place(x=100,y=180)

btn=Button(win,text="Save").place(x=60,y=240)
