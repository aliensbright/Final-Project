#!python3
'''
I will try to make a python sudoku with 10 different seeds

'''

import tkinter as tk
from tkinter import *
from tkinter import ttk
import math
import random
import time

for windowthings in range(1):
    win=tk.Tk()
    win.config(bg="#000000")
    win.geometry("250x230")
    boardframe=tk.Frame(bg="#000000")
    checkbutton=tk.Button(boardframe,text='Check')
    saveButton=tk.Button(win,text='Save')
    board=[]
    boardCreate=[]
    horLine=[]
    list_of_lines_or_board_squares=[]
    ogvalues=[]
    title=tk.Label(win,text='SUDOKU')
    button_setBoard=tk.Button(win,text='SET YOUR\nOWN GRID!')
    button_ranBoard=tk.Button(win,text='PLAY\nRANDOM!')
    Title=Label(boardframe,text='Sudoku')
    YouWin=Label(win,font=("Arial", 25),text='YOU \nWIN!!')
    play_again=tk.Button(text='Play again?')

def startgame():
    title.place(y=20,x=90)
    button_setBoard.place(y=100,x=30)
    button_ranBoard.place(y=100,x=130)

def createSeed(event):
    button_setBoard.place_forget()
    button_ranBoard.place_forget()
    title.place_forget()
    global board_forCreate
    board_forCreate=[]
    for blank in range(81):
        board_forCreate.append(tk.Entry(win,justify=CENTER,width=3,borderwidth=2,relief=RIDGE))
    for squares in board_forCreate:
        x=(board_forCreate.index(squares))%9+1
        y=math.floor((board_forCreate.index(squares)/9))+1
        vert=0
        horz=0
        if x%3==0:
            vert=4
        if y%3==0:
            horz=4
        squares.grid(row=y,column=x,padx=(0,vert),pady=(0,horz))
    saveButton.grid(row=10,column=4,columnspan=3)

def saveCreatedSeed(event):
    global ogvalues
    global board_forCreate
    global board
    ogvalues=[]
    for i in range(81):
        x=board_forCreate[i].get()
        if x=='':
            x=0
        else:
            x=int(x)
        ogvalues.append(x)
        x=''
        board_forCreate[i].grid_forget()
    saveButton.grid_forget()
    board=boardsetup(ogvalues)
    ogvalues=[]

def getSeed(event):
    global ogvalues
    global board
    button_setBoard.place_forget()
    button_ranBoard.place_forget()
    title.place_forget()
    ogvalues=[]
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
    ogvalues=seedList[x]
    #ogvalues=[1,2,0,4,5,6,7,8,9,4,5,6,7,8,9,1,2,3,0,8,9,1,2,3,4,5,6,2,3,1,5,6,4,8,0,7,5,6,4,8,9,7,2,3,1,8,9,7,2,3,1,5,6,4,3,1,2,6,4,5,9,7,8,6,4,5,9,7,8,3,1,2,9,7,8,3,1,2,6,4,5]
    board=boardsetup(ogvalues)
    ogvalues=[]

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

def boardsetup(values):
    global start_time
    tk.Label(text='     ',bg="#000000").grid(row=1,column=1)
    boardframe.grid(row=1,column=2,rowspan=10,columnspan=9)
    realgameboard=[]
    for num in values:
        try:
            assert 1<=num<=9
            assert type(num)==int
            realgameboard.append(tk.Label(boardframe,text=num,relief=RIDGE,width=2,bg='#ffffff',border=2,height=1,fg='#0000ff'))
        except:
            realgameboard.append(tk.Entry(boardframe,justify=CENTER,width=3,borderwidth=2,relief=RIDGE))
    for bored in realgameboard:
        x=(realgameboard.index(bored))%9+1
        y=math.floor((realgameboard.index(bored)/9))+1
        vert=0
        horz=0
        if x%3==0:
            vert=4
        if y%3==0:
            horz=4
        bored.grid(row=y,column=x,padx=(0,vert),pady=(0,horz))
    start_time=time.time()
    checkbutton.grid(row=0,column=7,columnspan=3)
    Title.grid(row=0,column=0,columnspan=10)
    return realgameboard

def getGridValues(filledboard):
    variableValues=[]
    for square in filledboard:
        try:
            x=square.get()
            x=int(x)
            assert 1<=x<=9
            variableValues.append(x)
        except:
            try:
                x=square.cget('text')
                x=int(x)
                assert 1<=x<=9
                variableValues.append(x)
            except:
                print('Please finish the grid with values from 1 - 9\n')
                break
    if len(variableValues)==81:
        return variableValues
    else:
        return None
   
def checkAnswer(event):
    global board
    global list_of_lines_or_board_squares
    global start_time
    variableBoard=getGridValues(board)
    horLine=[]
    check=True
    if variableBoard==None:
        pass
    else:
        en=True
        while check==True and en==True:
            for line in list_of_lines_or_board_squares:
                for box in line:
                    horLine.append(variableBoard[box])
                check=sortLists9(horLine)
                if line==list_of_lines_or_board_squares[26]:
                    en=False
                horLine=[]
                if check==False:
                    break
        if check==True:
            print('Correct, You Win\n')
            for i in board:
                i.grid_forget()
            boardframe.grid_forget()
            board=[]
            YouWin.place(x=70,y=75)
            final_timeMins=math.floor(round(time.time()-start_time,0)/60)
            final_timeSecs=int(round(time.time()-start_time,0)-60*final_timeMins)
            print(f'Time: {final_timeMins}:{final_timeSecs}')
            play_again.place(x=70,y=175)
        else:
            print('Incorrect, Please try again\n')

def playAgain(event):
    print('\nNew Game\n')
    YouWin.place_forget()
    play_again.place_forget()
    startgame()

def sortLists9(_9values): 
    _9values.sort(reverse=False)
    goodList=[1,2,3,4,5,6,7,8,9]
    if _9values==goodList:
        return True
    else:
        return False


lines()
startgame()
saveButton.bind('<Button>',saveCreatedSeed)
button_setBoard.bind('<Button>',createSeed)
button_ranBoard.bind('<Button>',getSeed)
checkbutton.bind('<Button>',checkAnswer)
play_again.bind('<Button>',playAgain)

win.mainloop()
