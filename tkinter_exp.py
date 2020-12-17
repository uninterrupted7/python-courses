# -*- coding: ut.f-8 -*-
"""
Created on Sat Dec 12 01:21:03 2020

@author: Abdurrahim
"""

from tkinter import *

window=Tk()

def from_kg():
    #convert kg to gram
    gram = float(e2_value.get()) * 100
    #convert kg to pound
    pound = float(e2_value.get()) * 2.20462
    
    #conver kg to ounce
    ounce = float(e2_value.get()) * 35.274
    
    #enter converted weight to the text widget
    t1.delete("1.0", END)
    t1.insert(END, gram)
    
    t2.delete("1.0", END)
    t2.insert(END, pound)
    
    t3.delete("1.0", END)
    t3.insert(END, ounce)
    
#create the label widgets

e1 = Label(window, text = "tl :")
e2_value = StringVar()
e2 = Entry(window, textvariable=e2_value)
e3 = Label(window, text='Gram')
e4 = Label(window, text = 'pounds')
e5 = Label(window, text = 'ounce')

#create text wigdets

t1 = Text(window, height=1, width=10)    
t2 = Text(window, height=1, width=40)
t3 = Text(window, height=1, width=40)

#create button

b1 = Button(window, text='cevir', command=from_kg)

#grid method placing for widgets positionsin table 

e1.grid(row=0, column=0)
e2.grid(row=0, column=1)
e3.grid(row=1, column=0)
e4.grid(row=1, column=1)
e5.grid(row=1, column=2)
t1.grid(row=2, column=0)
t2.grid(row=2, column=1)
t3.grid(row=2, column=2)
b1.grid(row=0, column=2)

#start GUI
window.mainloop()