#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from tkinter import *
master = Tk()
Label(master, text='Bookingid').grid(row=0)
Label(master, text='Passenger Name').grid(row=1)
Label(master, text='Flight').grid(row=2)
Label(master, text='Source').grid(row=3)
v = IntVar()
Radiobutton(master, text='Delhi', variable=v, value=1).grid(row=3,column=1)
Radiobutton(master, text='Mumbai', variable=v, value=1).grid(row=3,column=2)
Label(master, text='Destination').grid(row=3,column=3)
Radiobutton(master, text='Chennai', variable=v, value=1).grid(row=3,column=4)
Radiobutton(master, text='Kolkata', variable=v, value=1).grid(row=3,column=5)
Label(master, text='Duration').grid(row=4)
w = Spinbox(master, from_=0, to = 10)
w.grid(row=4, column = 1)
e1 = Entry(master)
e2 =  Entry(master)
e3 = Entry(master)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
insrt = Button(master, text= 'Insert', fg='black')
insrt.grid(row=5)
updte = Button(master, text= 'Update', fg='black')
updte.grid(row=5,column=1)
dlte = Button(master, text='Delete', fg='black')
dlte.grid(row=6)
slct = Button(master, text ='select', fg='black')
slct.grid(row=6,column=1)
mainloop()


# In[ ]:




