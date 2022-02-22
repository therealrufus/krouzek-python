import tkinter

window = tkinter.Tk()
window.title('Example')

canvas = tkinter.Canvas(window, width=600, height=600)

canvas.pack()

EMPTY = 0
RING = 1
CROSS = 2
DRAW = 3

board = [
    [EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY]
]

current_player = RING


def make_move(x: int, y: int):
    global current_player
    if board[x][y] == EMPTY:
        board[x][y] = current_player
        if current_player == RING:
            current_player = CROSS
        else:
            current_player = RING
        # Řádky
        if board[0][0] == board[0][1] and board[0][1] == board[0][2]:
            return board[0][0]
        if board[1][0] == board[1][1] and board[1][1] == board[1][2]:
            return board[1][0]
        if board[2][0] == board[2][1] and board[2][1] == board[2][2]:
            return board[2][0]
        # Sloupce
        if board[0][0] == board[1][0] and board[1][0] == board[2][0]:
            return board[0][0]
        if board[0][1] == board[1][1] and board[1][1] == board[2][1]:
            return board[0][1]
        if board[0][2] == board[1][2] and board[1][2] == board[2][2]:
            return board[0][2]
        # Diagonály
        if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
            return board[0][0]
        if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
            return board[0][2]
        for x in range(0, 3):
            for y in range(0, 3):
                if board[x][y] == EMPTY:
                    return EMPTY
        return DRAW

make_move(0, 0)
make_move(0, 1)
make_move(2, 2)
make_move(1, 2)

def draw():
    canvas.create_rectangle(0, 0, 600, 600, fill="#FFFFFF")
    canvas.create_line(0, 200, 600, 200, fill="#000000", width=5)
    canvas.create_line(0, 400, 600, 400, fill="#000000", width=5)
    canvas.create_line(200, 0, 200, 600, fill="#000000", width=5)
    canvas.create_line(400, 0, 400, 600, fill="#000000", width=5)
    for x in range(0, 3):
        for y in range(0, 3):
            if board[x][y] == CROSS:
                canvas.create_line(40+200*x, 40+200*y, 160+200*x, 160+200*y, fill="#0000FF", width=5)
                canvas.create_line(160+200*x, 40+200*y, 40+200*x, 160+200*y, fill="#0000FF", width=5)
            elif board[x][y] == RING:
                canvas.create_oval(40+200*x, 40+200*y, 160+200*x, 160+200*y, outline="#FF0000", width=5)

draw()

window.mainloop()
