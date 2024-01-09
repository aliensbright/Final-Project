#!python3
'''
I will try to make a python sudoku with 10 different seeds

'''

import tkinter as tk
from tkinter import *
from tkinter import ttk
import math

win=tk.Tk()

values=[0,8,0,0,0,0,0,3,0,2,0,0,6,0,7,0,0,1,0,0,0,0,0,0,0,0,0,0,6,0,2,0,1,0,7,0,5,0,0,0,0,0,0,0,3,9,0,0,7,0,5,0,0,8,4,0,1,3,0,9,7,0,6,0,2,0,0,0,0,0,1,0,8,0,3,1,0,6,5,0,9]

board=[]

def boardsetup(values,board):
    for num in values:
        if num!=0:
            board.append(tk.Label(text=num,width=2))
        else:
            board.append(tk.Entry(text='',width=2))
    for bored in board:
        x=(board.index(bored))%9
        y=math.floor((board.index(bored)/9))
        bored.grid(row=y,column=x)
    
#0,8,0,0,0,0,0,3,0
#2,0,0,6,0,7,0,0,1
#0,0,0,0,0,0,0,0,0
#0,6,0,2,0,1,0,7,0
#5,0,0,0,0,0,0,0,3
#9,0,0,7,0,5,0,0,8
#4,0,1,3,0,9,7,0,6
#0,2,0,0,0,0,0,1,0
#8,0,3,1,0,6,5,0,9
boardsetup(values,board)
win.mainloop()
