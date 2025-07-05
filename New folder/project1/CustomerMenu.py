
from tkinter import *

win = Tk()
win.title("Custom Menu")
win.geometry('900x700')


Pic = PhotoImage(master=win,file="images.png")
Pic_label = Label(win,image=Pic).grid(row=0,column=0,rowspan=10,columnspan=10)

def New():
    win.destroy()
    import DetailWindow

def Back():
    win.destroy()
    import Menu

btn=Button(win,text="Create New Account",height =3, width = 15,command=New).grid(row=2,column=3)

btn1=Button(win,text="Show Account",height =3, width = 15).grid(row=2,column=6)

btn2=Button(win,text="Deposit",height =3, width = 15).grid(row=4,column=3)

btn3=Button(win,text="Withdraw",height =3, width = 15).grid(row=4,column=6)

btn4=Button(win,text="Update",height =3, width = 15).grid(row=5,column=3)

btn5=Button(win,text="Drop Account",height =3, width = 15).grid(row=5,column=6)

btn6=Button(win,text="Back to menu",height =3, width = 15,command=Back).grid(row=6,column=4)
