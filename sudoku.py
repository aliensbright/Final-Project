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
horLine=[]
list_of_lines_or_board_squares=[]
Title.grid(row=0,column=0,columnspan=10)
checkbutton.grid(row=0,column=7,columnspan=3)

def lines():
    global horLine
    global list_of_lines_or_board_squares
    for multiple in range(9):
        for modVal in range(9):
            horLine.append(multiple*9+modVal)
        list_of_lines_or_board_squares.append(horLine)
        horLine=[]
    for multiple in range(9):
        for modVal in range(9):
            horLine.append(modVal*9+multiple)
        list_of_lines_or_board_squares.append(horLine)
        horLine=[]
    for xBox in range(3):
        for yBox in range(3):
            for multiple in range(3*yBox,3*yBox+3):
                for modVal in range(3*xBox,3*xBox+3):
                    horLine.append(modVal*9+multiple)
            list_of_lines_or_board_squares.append(horLine)
            horLine=[]


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
            assert 1<=x<=9
            variableValues.append(x)
        except:
            try:
                x=square.cget('text')
                x=int(x)
                variableValues.append(x)
                assert 1<=x<=9
            except:
                print('Please finish the grid with values from 1 - 9')
                break
    if len(variableValues)==81:
        return variableValues
    else:
        return None
    
    
def checkAnswer(event):
    global board
    global list_of_lines_or_board_squares
    variableBoard=getGridValues(board)
    horLine=[]
    check=True
    if variableBoard==None:
        pass
    else:
        while check==True:
            for line in list_of_lines_or_board_squares:
                for box in line:
                    horLine.append(variableBoard[box])
                check=sortLists9(horLine)
                horLine=[]
        print('Incorrect, Please try again')
        
        
def sortLists9(_9values): #type list
    _9values.sort()
    goodList=(1,2,3,4,5,6,7,8,9)
    if _9values==goodList:
        return True
    else:
        return False
lines()


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
