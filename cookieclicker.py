from enum import auto
from tkinter import *
import time, threading
root = Tk()

root.counter = 0
root.multiplier = 1
root.autoNumber = 0
root.autoSpeed = 1

img = PhotoImage(file="sabloprisme.png") 
def clicked():
    root.counter += root.multiplier
    L['text'] = 'Button clicked: ' + str(root.counter)
        
def addMulti():
    if(root.counter > 50*root.multiplier):
        root.counter -= 50*root.multiplier
        root.multiplier += 1  
        mc['text'] = f'Get click multiplier: {50*root.multiplier}'
        ML['text'] = 'Multiplier: ' + str(root.multiplier)

def autoclick():
    print(time.ctime())
    root.counter += root.autoNumber
    L['text'] = 'Button clicked: ' + str(root.counter)
    threading.Timer(5/root.autoSpeed, autoclick).start()

def addAuto():
    if(root.counter > 100*root.autoNumber+1):
        root.counter -= 100*root.autoNumber+1
        root.autoNumber +=1
        AL['text'] = 'Autoclickers: ' + str(root.autoNumber)
        acm['text'] = f'Get autoclicker: {100*root.autoNumber+1}'
        autoclick()

def addSpeed():
    if(root.counter > 75*root.autoSpeed):
        root.counter -= 75*root.autoSpeed
        root.autoSpeed +=1
        acs['text'] = f'Faster autoclicker: {75*root.autoSpeed}'
        SL['text'] = 'Speed: ' + str(root.autoSpeed)

b = Button(root,image=img ,text="Click Me", command=clicked)
b.pack()

acm = Button(root, text=f"Get autoclicker (100 clicks)", command=addAuto)
acm.pack()

acs = Button(root, text=f"Faster autoclicker (75 clicks)", command=addSpeed)
acs.pack()

mc = Button(root, text=f"Get click multiplier (50 clicks)", command=addMulti)
mc.pack()

L = Label(root, text="No clicks yet.")
L.pack()

ML = Label(root, text="No multiplier yet")
ML.pack()

AL = Label(root, text="No autoclickers yet")
AL.pack()

SL = Label(root, text="No autoclickers yet")
SL.pack()

root.mainloop()   