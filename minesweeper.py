from random import Random, random
import tkinter

root = tkinter.Tk()
canvas = tkinter.Canvas(root, width=600, height=600)
canvas.pack()

class Board():
    def __init__(self, size):
        self.size = size
        self.playingField = [["0" for i in range(size)] for j in range(size)]
        self.rnd = Random()
    
    def generateField(self, difficulty):
        #fill mines
        for x in range(self.size):
            for y in range(self.size):
                if self.rnd.randint(0, 4) == 1: 
                    self.playingField[x][y] = ("x")
        
        #fill numbers
        for x in range(self.size):
            for y in range(self.size):
                if(self.playingField[x][y] != "x"):
                    nearBombs = 0
                    nearBombs = nearBombs + (self.checkBomb(x-1, y-1))
                    nearBombs = nearBombs + (self.checkBomb(x, y-1))
                    nearBombs = nearBombs + (self.checkBomb(x+1, y-1))
                    nearBombs = nearBombs + (self.checkBomb(x-1, y))
                    nearBombs = nearBombs + (self.checkBomb(x+1, y))
                    nearBombs = nearBombs + (self.checkBomb(x-1, y+1))
                    nearBombs = nearBombs + (self.checkBomb(x, y+1))
                    nearBombs = nearBombs + (self.checkBomb(x+1, y+1))
                    
                    self.playingField[x][y] = nearBombs

    def checkBomb(self, xb, yb):
        if (0 <= xb < self.size) & (0 <= yb < self.size):
            if self.playingField[xb][yb] == "x":
                print(f"na {xb}, {yb} je bomba")
                return 1
            else:
                print(f"na {xb}, {yb} není bomba")
                return 0
        return 0
        
    def printField(self):
        print('\n'.join(' '.join(str(x) for x in row) for row in self.playingField))

canvas.update()
def draw():
    canvas.create_rectangle(0, 0, 800, 800, fill="#FFFFFF")
    for i in range(board.size):
        canvas.create_line(CellSize*i, 0, CellSize*i, 800, fill="#000000", width=3)
        canvas.create_line(0, CellSize*i, 800, CellSize*i, fill="#000000", width=3)

    for x in range(0, board.size):
        for y in range(0, board.size):
            if board.playingField[x][y] == "x":
                pass
                #canvas.create_oval(10+CellSize*x, 10+CellSize*y, 50+CellSize*x, 50+CellSize*y, outline="#FF0000", fill="#FF0000", width=3)
            elif board.playingField[x][y] == "0":
                pass

def rightClick(event):
    col = 0
    row = 0
    x, y = event.x, event.y
    row = int(x/canvas.winfo_height()*board.size)
    col = int(y/canvas.winfo_height()*board.size)
    canvas.create_oval(10+CellSize*row, 10+CellSize*col, 50+CellSize*row, 50+CellSize*col, outline="#000000", fill="#a1ff4a", width=3)

def leftClick(event):
    col = 0
    row = 0
    x, y = event.x, event.y
    row = int(x/canvas.winfo_height()*board.size)
    col = int(y/canvas.winfo_height()*board.size)
    if board.playingField[col][row] != "x":
        canvas.create_text(30+CellSize*row, 30+CellSize*col, font="Calibri 20",text=board.playingField[col][row])        

    elif board.playingField[col][row] == "x":
        canvas.create_oval(10+CellSize*row, 10+CellSize*col, 50+CellSize*row, 50+CellSize*col, outline="#FF0000", fill="#FF0000", width=3)

    else:
        canvas.create_rectangle(10+CellSize*row, 10+CellSize*col, 50+CellSize*row, 50+CellSize*col, outline="#000000", fill="#bebebe", width=3)
        
root.bind("<Button-3>", rightClick)
root.bind("<Button-1>", leftClick)

board = Board(10)
CellSize = root.winfo_width()/board.size
board.generateField(5)
board.printField()
draw()

root.mainloop()