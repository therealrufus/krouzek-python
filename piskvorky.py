from itertools import count
from operator import pos
from re import X
from socket import INADDR_BROADCAST
import tkinter
from tkinter import W, Canvas, messagebox
from tkinter.ttk import Sizegrip

window = tkinter.Tk()
window.title('Example')

canvas = tkinter.Canvas(window, width=800, height=800)

canvas.pack()

EMPTY = 0
RING = 1
CROSS = 2
DRAW = 3

size = 8
winCount = 5

board = [[EMPTY for i in range(size)] for j in range(size)]

current_player = RING

def make_move(x: int, y: int):    
    global current_player
    if board[x][y] == EMPTY:
        board[x][y] = current_player

        if checkWin(current_player) == 1:
            return board[x][y]

        if current_player == RING:
            current_player = CROSS
        else:
            current_player = RING
        for x in range(0, size):
            for y in range(0, size):
                if board[x][y] == EMPTY:
                    return EMPTY
        return DRAW


def draw():
    CellSize = canvas.winfo_height()/size
    canvas.create_rectangle(0, 0, 800, 800, fill="#FFFFFF")
    for i in range(size):
        canvas.create_line(CellSize*i, 0, CellSize*i, 800, fill="#000000", width=5)
        canvas.create_line(0, CellSize*i, 800, CellSize*i, fill="#000000", width=5)
        

    for x in range(0, size):
        for y in range(0, size):
            if board[x][y] == CROSS:
                canvas.create_line(20+100*x, 20+100*y, 80+100*x, 80+100*y, fill="#0000FF", width=5)
                canvas.create_line(80+100*x, 20+100*y, 20+100*x, 80+100*y, fill="#0000FF", width=5)
            elif board[x][y] == RING:
                canvas.create_oval(20+100*x, 20+100*y, 80+100*x, 80+100*y, outline="#FF0000", width=5)


def clear():
    for x in range(0, size):
        for y in range(0, size):
            board[x][y] = EMPTY
    draw()


def on_mouse_click(event):
    # print(str(event.x) + "  " + str(event.y))
    col = 0
    row = 0
    x, y = event.x, event.y
    # col = 0
    # if x < 100:
    #     col = 0
    # elif 100 <= x < 400:
    #     col = 1
    # else:
    #     col = 2
    col = int(x/canvas.winfo_height()*size)
    row = int(y/canvas.winfo_height()*size)
    
    print(f"{x} > {col}, {y} > {row}")
    winner = make_move(col, row)
    draw()
    if winner == RING:
        response = tkinter.messagebox.askquestion("Vyhrálo kolečko", "Vyhrálo kolečko. Chceš hrát znovu?", icon="info")
        if response == "yes":
            clear()
        else:
            window.quit()
    elif winner == CROSS:
        response = tkinter.messagebox.askquestion("Vyhrál křížek", "Vyhrál křížek. Chceš hrát znovu?", icon="info")
        if response == "yes":
            clear()
        else:
            window.quit()
    elif winner == DRAW:
        response = tkinter.messagebox.askquestion("Remíza", "Remíza. Chceš hrát znovu?", icon="info")
        if response == "yes":
            clear()
        else:
            window.quit()


def on_resize(event):
    draw()

def checkWin(player):
    #player = current symbol
    #inARow = how many in a row are there

    #check all rows
    inARow = 0
    for i in range(size):
        for j in range(size):
            if board[j][i] == player:
                inARow = inARow + 1
                #print(f"{j},{i} = {player}")
                if inARow == winCount:
                    return 1
            elif board[j][i] != player:
                inARow = 0
                #print(f"{j},{i} = {0}")
            if j == 7:
                inARow = 0

    #check all coulmns
    inARow = 0
    for i in range(size):
        for j in range(size):
            if board[i][j] == player:
                inARow = inARow + 1
                #print(f"{i},{j} = {player}")
                if inARow == winCount:
                    return 1
            elif board[i][j] != player:
                inARow = 0
                #print(f"{i},{j} = {0}")
            if j == 7:
                inARow = 0

    #check upper diagonals right to left
    inARow = 0
    for ix in range(size):
        for d in range(ix+1):
            if board[ix-d][d] == player:
                #print(f"{ix-d},{d} = {player}")
                inARow = inARow + 1
                if inARow == winCount:
                    return 1
                elif board[ix-d][d] != player:
                    inARow = 0 
        inARow = 0

    #check lower diagonals right to left
    inARow = 0
    for ix in range(size):
        for d in range(ix+1):
            #print(f"{ix},{d}")
            posX = size - ix  + d -1
            posY = size - d - 1
            #print(f"{posX},{posY} == {ix - d}, {d}")
            if board[posX][posY] == player:
                inARow = inARow + 1
                if inARow == winCount:
                    return 1
                elif board[posX][posY] != player:
                    inARow = 0 
        inARow = 0

    #check upper diagonals left to right
    inARow = 0
    for ix in range(size):
        for d in range(ix+1):
            #print(f"x:{ix} d:{d}, x,y({size-ix-1+d},{d})")
            if board[size-ix-1+d][d] == player:
                inARow = inARow + 1
                if inARow == winCount:
                    return 1
                elif board[size-ix-1+d][d] != player:
                    inARow = 0 
        inARow = 0

    #check lower diagonals left to right
    inARow = 0
    for ix in range(size):
        for d in range(ix+1):
            #print(f"{ix},{d}")
            posX = ix - d
            posY = size - d - 1
            #print(f"{posX},{posY} == {ix}, {d}")
            if board[posX][posY] == player:
                inARow = inARow + 1
                if inARow == winCount:
                    return 1
                elif board[posX][posY] != player:
                    inARow = 0 
        inARow = 0

tkinter.Grid.rowconfigure(window,0,weight=1)
tkinter.Grid.columnconfigure(window,0,weight=1)
canvas.grid(row=0,column=0,sticky="NSEW")

window.bind("<Button-1>", on_mouse_click)
window.bind("<Configure>", on_resize)

draw()

window.mainloop()
