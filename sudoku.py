#!python3
'''
I will try to make a python sudoku with 10 different seeds

'''

import tkinter as tk
from tkinter import *
from tkinter import ttk
import math

win=tk.Tk()
win.config(bg="#000000")
ogvalues=[0,8,0,0,0,0,0,3,0,2,0,0,6,0,7,0,0,1,0,0,0,0,0,0,0,0,0,0,6,0,2,0,1,0,7,0,5,0,0,0,0,0,0,0,3,9,0,0,7,0,5,0,0,8,4,0,1,3,0,9,7,0,6,0,2,0,0,0,0,0,1,0,8,0,3,1,0,6,5,0,9]
checkbutton=tk.Button(text='Check')
Title=Label(text='Sudoku')
board=[]
Title.grid(row=0,column=0,columnspan=10)
checkbutton.grid(row=0,column=7,columnspan=3)

def boardsetup(values,board):
    for num in values:
        if num!=0:
            board.append(tk.Label(text=num,relief=RIDGE,width=2,bg='#ffffff',border=2,height=1,fg='#0000ff'))
        else:
            board.append(tk.Entry(justify=CENTER,width=3,borderwidth=2,relief=RIDGE))
    for bored in board:
        x=(board.index(bored))%9+1
        y=math.floor((board.index(bored)/9))+1
        vert=0
        horz=0
        print(x,y,bored)
        if x%3==0:
            vert=4
        if y%3==0:
            horz=4
        bored.grid(row=y,column=x,padx=(0,vert),pady=(0,horz))
 
def getGridValues(board):
    variableValues=[]
    for square in board:
        try:
            x=square.get()
            x=int(x)
            variableValues.append(x)
        except:
            try:
                x=square.cget('text')
                x=int(x)
                variableValues.append(x)
            except:
                print('Please finish the grid')
                break
    if len(variableValues)==81:
        return variableValues
    else:
        return None
    
    
def checkAnswer(event):
    global board
    variableBoard=getGridValues(board)
    lineOrBox=[]
    if variableBoard==None:
        pass
    else:
        pass

        
def sortLists9(_9values): #type list
    _9values.sort()
    goodList=(1,2,3,4,5,6,7,8,9)


'''
for i in range 9:
    lineOrBox.append(variableboard%9+i)
( 0,9,18,27,36,45,54,63,72)
(1,10,19,28,37,46,55,64,73)

'''

#0,8,0,0,0,0,0,3,0 
#2,0,0,6,0,7,0,0,1 
#0,0,0,0,0,0,0,0,0 
#0,6,0,2,0,1,0,7,0 
#5,0,0,0,0,0,0,0,3 
#9,0,0,7,0,5,0,0,8 
#4,0,1,3,0,9,7,0,6 
#0,2,0,0,0,0,0,1,0 
#8,0,3,1,0,6,5,0,9 
boardsetup(ogvalues,board)
checkbutton.bind('<Button>',checkAnswer)
win.mainloop()
