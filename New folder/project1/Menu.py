from tkinter import *

#Main Menu

Top = Tk()
Top.title("Main Window")
Top.geometry('900x700')

Pic = PhotoImage(master=Top,file="images.png")
Pic_label = Label(Top,image=Pic).grid(row=0,column=0,rowspan=10,columnspan=10)

def cust():
    Top.destroy()
    import CustomerMenu

def emp():
    Top.destroy()
    import Elogin_gui


Cust = Button(Top,font=('Roboto',12),text="Customer Menu", height =3, width = 13, command=cust)
Cust.grid(column=2, row=7)

Emp = Button(Top,font=('Roboto',12), text="Employee Menu",height =3, width = 13, command=emp)
Emp.grid(column=5, row=7,columnspan=2)

