from tkinter import *
import tkinter

root = Tk()
root.title("rekurze")

wd = 600
he = 600
CubeAmount = 3
iterations = 0

canvas = tkinter.Canvas(root, width=wd, height=he)
canvas.pack()

velikost = wd/CubeAmount

def DrawCube(size, iter):
    iter +=1
    if iter > 2:
        return
    else:
        for i in range(3):
            for j in range(3):
                canvas.create_rectangle(i*size, j*size, i*size+size, j*size+size, outline="#ffffff", fill="#000000")
                DrawCube(size/3, iter)

DrawCube(velikost, iterations)
root.mainloop()