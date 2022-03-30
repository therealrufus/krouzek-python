import tkinter
from random import Random, random

root = tkinter.Tk()
canvas = tkinter.Canvas(root, width=600, height=600)
canvas.pack()

size = 10
bombs = 15

class Board():
    def __init__(self, size, bombs):
        self.size = size
        self.bombs = bombs
        self.rnd = Random()
        self.field = [["0" for i in range(self.size)] for j in range(self.size)]

    def printField(self):
        print('\n'.join(' '.join(str(x) for x in row)for row in self.field))

    def generate(self):
        for i in range(self.bombs):
            randomX = self.rnd.randint(0, self.size-1)
            randomY = self.rnd.randint(0, self.size-1)

            self.field[randomX][randomY] = "x"

        for x in range(self.size):
            for y in range(self.size):
                if self.field[x][y] != "x":
                    closeBombs = 0
                    closeBombs += self.checkBombs(x, y+1)
                    closeBombs += self.checkBombs(x, y-1)
                    closeBombs += self.checkBombs(x-1, y+1)
                    closeBombs += self.checkBombs(x-1, y-1)
                    closeBombs += self.checkBombs(x-1, y)
                    closeBombs += self.checkBombs(x+1, y+1)
                    closeBombs += self.checkBombs(x+1, y-1)
                    closeBombs += self.checkBombs(x+1, y)

                    self.field[x][y] = closeBombs
                    print(closeBombs)

    def checkBombs(self, x, y):
        if(0 <= x < self.size) & (0 <= y < self.size):
            if self.field[x][y] == "x":
                print(f"{x} {y}, je bomba")
                return 1
            else:
                return 0
        return 0

def draw():
    for i in range(board1.size):
        canvas.create_line()


board1 = Board(size, bombs)
CellSize = root.winfo_height/board1.size
board1.generate()
board1.printField()