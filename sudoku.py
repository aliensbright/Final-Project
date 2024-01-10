#!python3
'''
I will try to make a python sudoku with 10 different seeds

'''

import tkinter as tk
from tkinter import *
from tkinter import ttk
import math

win=tk.Tk()
win.config(bg="#0000ff")
values=[0,8,0,0,0,0,0,3,0,2,0,0,6,0,7,0,0,1,0,0,0,0,0,0,0,0,0,0,6,0,2,0,1,0,7,0,5,0,0,0,0,0,0,0,3,9,0,0,7,0,5,0,0,8,4,0,1,3,0,9,7,0,6,0,2,0,0,0,0,0,1,0,8,0,3,1,0,6,5,0,9]


board=[]


#def boardsetup(values,board):
#    for num in values:
#        if num!=0:
#            board.append(tk.Label(text=num,width=2,bg='#ffffff',height=1,fg='#0000ff'))
#        else:
#            board.append(tk.Entry(text='',width=3,borderwidth=0))
#    for bored in board:
#        x=(board.index(bored))%9
#        y=math.floor((board.index(bored)/9))
#        bored.grid(row=y,column=x)
    

    
#0,8,0,0,0,0,0,3,0
#2,0,0,6,0,7,0,0,1
#0,0,0,0,0,0,0,0,0
#0,6,0,2,0,1,0,7,0
#5,0,0,0,0,0,0,0,3
#9,0,0,7,0,5,0,0,8
#4,0,1,3,0,9,7,0,6
#0,2,0,0,0,0,0,1,0
#8,0,3,1,0,6,5,0,9
#boardsetup(values,board)

hor1=hor2=hor3=hor4=hor5=hor6=hor7=hor8=Label(image=(PhotoImage(file='Images/HorizontalLine.png',height=1)))
verLine=Label(image=(PhotoImage(file='Images/VerticalLine.png')))

lines=((hor1,100,100),(hor2,200,200),(hor3,300,300),(hor4,400,0),(hor5,500,0),(hor6,600,0),(hor7,700,0),(hor8,800,0))

for gridLines in lines:
    print(gridLines)
    gridLines[0].place(y=gridLines[1],x=gridLines[2])

win.mainloop()
