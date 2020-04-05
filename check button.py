from tkinter import *
m=Tk()
var1=IntVar()
Checkbutton(m,text='male',variable=var1).grid(row=10,column=100)
var2=IntVar()
Checkbutton(m,text='female',variable=var2).grid(row=20,column=100)
m.mainloop()
