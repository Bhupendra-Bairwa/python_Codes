from tkinter import *
Top = Tk()

Top.geometry('500x500')

def fream():
    Top.destroy
    import fream

name=Label(Top,text="Name").place(x=20,y=40)
e1=Entry(Top).place(x=80,y=40)

email=Label(Top,text="Email").place(x=250,y=40)
e2=Entry(Top).place(x=350,y=40)

address=Label(Top,text="Address").place(x=20,y=80)
e3=Entry(Top).place(x=80,y=80)

contect=Label(Top,text="Contect").place(x=250,y=80)
e4=Entry(Top).place(x=350,y=80)

btn=Button(Top,text="Save",command=fream).place(x=50,y=100)
