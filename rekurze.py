from email.mime import multipart
from tkinter import *
import tkinter
from turtle import color

root = Tk()
root.title("rekurze")

wd = 600
he = 600
thickness = 8
barva = "#6d8f76"
iterations = 0
multiplier = 10

canvas = tkinter.Canvas(root, width=wd, height=he)
canvas.pack()

def DrawCircle(x1, y1, x2, y2, width):
    global iterations
    iterations += 1
    canvas.create_oval(x1, y1, x2, y2, width=width)
    if iterations < 30:
        DrawCircle(iterations*multiplier, iterations*multiplier, wd-iterations*multiplier, he-iterations*multiplier, thickness)
    else:
        return

DrawCircle(0, 0, wd, he, thickness)
root.mainloop()