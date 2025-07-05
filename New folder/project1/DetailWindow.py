from tkinter import *

top = Tk()
top.title("Detail Window")
top.geometry('900x700')


Pic = PhotoImage(master=top,file="images.png")
Pic_label = Label(top,image=Pic).grid(row=0,column=0,rowspan=10,columnspan=10)

def Dist():
    top.destroy()
    import CustomerMenu

n1=Label(top,text="Cust.Name:").grid(row=0,column=0)
e1=Entry(top).grid(row=0,column=1)

n1=Label(top,text="Cust.Mail Id:").grid(row=1,column=0)
e1=Entry(top).grid(row=1,column=1)

n1=Label(top,text="Cust.Password").grid(row=2,column=0)
e1=Entry(top).grid(row=2,column=1)

n1=Label(top,text="Cust.ContactNo:").grid(row=3,column=0)
e1=Entry(top).grid(row=3,column=1)

n1=Label(top,text="Cust.Age:").grid(row=4,column=0)
e1=Entry(top).grid(row=4,column=1)

n1=Label(top,text="Opening Amount:").grid(row=5,column=0)
e1=Entry(top).grid(row=5,column=1)

n1=Label(top,text="Gender").grid(row=6,column=0)
e1=Entry(top).grid(row=6,column=1)

n1=Label(top,text="Date of Creation").grid(row=7,column=0)
e1=Entry(top).grid(row=7,column=1)

btn=Button(top,text="Today's Date",height =2, width = 10).grid(row=7,column=4)


btn=Button(top,text="Insert Detail",height =2, width = 10).grid(row=8,column=2)

btn=Button(top,text="Back to Cust Menu",height =2, width = 15,command=Dist).grid(row=8,column=4)


