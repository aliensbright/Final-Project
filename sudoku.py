#!python3
'''
I will try to make a python sudoku with 10 different seeds

'''

import tkinter as tk
from tkinter import *
from tkinter import ttk
import math
import random

win=tk.Tk()
win.config(bg="#000000")
win.geometry("230x230")
win.resizable(False,False)
checkbutton=tk.Button(text='Check')
Title=Label(text='Sudoku')
board=[]
horLine=[]
list_of_lines_or_board_squares=[]
Title.grid(row=0,column=0,columnspan=10)
checkbutton.grid(row=0,column=7,columnspan=3)

def getSeed():
    s1=(0,8,0,0,0,0,0,3,0,2,0,0,6,0,7,0,0,1,0,0,0,0,0,0,0,0,0,0,6,0,2,0,1,0,7,0,5,0,0,0,0,0,0,0,3,9,0,0,7,0,5,0,0,8,4,0,1,3,0,9,7,0,6,0,2,0,0,0,0,0,1,0,8,0,3,1,0,6,5,0,9)
    s2=(3,0,0,8,0,1,0,0,2,2,0,1,0,3,0,6,0,4,0,0,0,2,0,4,0,0,0,8,0,9,0,0,0,1,0,6,0,6,0,0,0,0,0,5,0,7,0,2,0,0,0,4,0,9,0,0,0,5,0,9,0,0,0,9,0,4,0,8,0,7,0,5,6,0,0,1,0,7,0,0,3)
    s3=(5,3,0,0,7,0,0,0,0,6,0,0,1,9,5,0,0,0,0,9,8,0,0,0,0,6,0,8,0,0,0,6,0,0,0,3,4,0,0,8,0,3,0,0,1,7,0,0,0,2,0,0,0,6,0,6,0,0,0,0,2,8,0,0,0,0,4,1,9,0,0,5,0,0,0,0,8,0,0,7,9)
    s4=(0,9,2,5,4,0,0,0,3,0,0,0,0,0,2,0,0,0,6,0,4,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,8,9,0,4,0,0,5,0,0,0,6,8,0,9,0,0,0,4,0,0,0,0,0,1,9,8,2,0,0,0,5,0,0,0,5,0,1,0,0,0,8,0,0)
    s5=(4,3,5,0,0,0,6,9,0,0,7,0,3,0,9,1,0,5,0,0,1,0,5,0,3,0,7,0,0,3,4,2,0,8,0,0,8,6,0,9,0,0,0,0,4,5,0,4,0,0,3,0,1,0,7,4,0,1,3,0,0,0,0,6,1,0,5,9,0,0,0,0,0,0,8,0,6,4,0,0,1)
    s6=(4,0,0,1,5,7,0,8,3,0,0,0,0,0,6,5,0,4,7,5,0,2,0,0,0,0,9,0,2,7,0,0,0,3,6,0,0,3,1,0,7,0,0,0,8,0,0,9,8,0,0,0,0,5,9,0,0,0,0,0,0,0,0,0,0,0,0,0,3,9,0,0,0,7,4,0,2,0,0,0,0)
    s7=(0,0,0,0,1,3,0,0,7,4,0,0,0,8,0,0,1,5,0,0,7,0,5,4,6,0,0,2,0,0,0,0,5,0,0,1,5,0,0,7,2,6,0,0,9,7,0,0,0,9,0,0,0,0,0,6,0,0,0,0,0,0,2,0,2,9,0,3,0,0,6,0,0,0,0,1,0,0,5,0,8)
    s8=(0,6,5,0,4,0,0,0,1,0,0,0,0,6,0,0,0,0,2,0,3,1,0,5,6,0,8,5,8,6,3,0,2,0,9,0,4,3,0,0,5,0,0,0,0,0,0,0,6,0,4,0,0,3,0,0,9,7,0,0,3,5,0,1,0,8,0,0,9,0,6,2,0,7,4,5,0,0,8,1,9)
    s9=(0,0,0,0,8,0,1,0,0,0,4,3,0,0,0,0,7,6,7,0,1,0,0,4,0,0,0,0,0,0,0,5,6,7,0,9,5,0,0,0,4,0,0,1,8,0,3,0,0,0,7,0,0,0,0,6,0,9,0,8,0,0,0,3,8,5,1,0,2,4,0,7,9,0,7,4,0,5,6,8,2)
    s0=(6,0,5,9,0,0,0,0,3,2,0,0,0,0,3,0,0,0,0,1,3,0,0,8,6,7,0,3,9,8,0,0,0,4,6,5,0,0,0,3,8,0,0,9,0,0,0,0,0,0,0,0,3,0,7,0,2,0,0,0,0,4,6,4,6,0,5,0,7,0,0,0,0,0,0,0,0,6,7,0,9)
    seedList=[s1,s2,s3,s4,s5,s6,s7,s8,s9,s0]
    x=random.randint(0,9)
    seedFinal=seedList[x]
    return seedFinal

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

ogvalues=getSeed()
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
