from tkinter import *
i = 2
x = 150
y = 0
a = 175
b = 25


def move():
    global x, y, a, b, i, ov
    y += 20
    b += 20
    if b >= 300:
        fen.quit()

    can.coords(ov, x, y, a, b)

    if i != 0:
        fen.after(200, move)


fen = Tk()
can = Canvas(fen, width=300, height=300, bg='dark grey')
can.pack()

ov = can.create_oval(x, y, a, b, fill='red')
Button(fen, text='start', command=move).pack()
fen.mainloop()
