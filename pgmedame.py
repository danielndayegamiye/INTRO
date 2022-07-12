from tkinter import *
from random import *


def damier():
    global x, y
    i = 0
    n = 0
    while i < 10:
        x = 0
        while x <= 200:
            if n % 2 == 0:
                can.create_rectangle(x, y + 20, x + 20, y, fill='black')
            else:
                can.create_rectangle(x, y + 20, x + 20, y, fill='ivory')
            n += 1
            x += 20
        y += 20
        i += 1


def pion():
    "pgme dessinant1 les pions de façon aleatoire nb: fonction pas comprise"

    a = randrange(10)*20+5
    b = randrange(10)*20+5
    can.create_oval(a, b, a+10, b+10, fill='red')


x, y = 0, 0
fen = Tk()
can = Canvas(fen, width=198, height=200, bg='ivory')
can.pack(padx=5, pady=5)
but1 = Button(fen, text='Damier', command=damier)
but1.pack(padx=3, pady=3)
but2 = Button(fen, text='Pion', command=pion)
but2.pack()
fen.mainloop()
