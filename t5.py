import tkinter
from tkinter import *
r=tkinter.Tk()
r.title('Registration Form')
Label(r,text='Name').grid(row=0)
Label(r,text='Age').grid(row=1)
Label(r,text='E-mail').grid(row=2)
Label(r,text='Phone').grid(row=3)
Label(r,text='Department').grid(row=4)
w1=Entry(r)
w2=Entry(r)
w3=Entry(r)
w4=Entry(r)
w5=Entry(r)
w1.grid(row=0,column=1)
w2.grid(row=1,column=1)
w3.grid(row=2,column=1)
w4.grid(row=3,column=1)
w5.grid(row=4,column=1)


def show_entries():
    txtN=w1.get()
    txtA=w2.get()
    txtE=w3.get()
    txtP=w4.get()
    txtD=w5.get()
    print(txtN,txtA,txtE,txtP,txtD)



t=tkinter.Button(r, text= 'Entry',bg= 'purple',command=show_entries)
t.grid(row=5, column=1)
r.mainloop()