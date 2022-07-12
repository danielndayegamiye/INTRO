# pgme permettant de controler la position de 2 astres

from tkinter import *


def avance(n, gd, hb):
    global x, y, astre
    x[n] += gd
    y[n] += hb
    can.coords(astre[n], x[n], y[n], x[n]+30, y[n]+30)


def depl_gauche1():
    avance(0, -10, 0)


def depl_droite1():
    avance(0, 10, 0)


def depl_haut1():
    avance(0, 0, -10)


def depl_bas1():
    avance(0, 0, 10)


def depl_gauche2():
    avance(1, -10, 0)


def depl_droite2():
    avance(1, 10, 0)


def depl_haut2():
    avance(1, 0, -10)


def depl_bas2():
    avance(1, 0, 10)


def cercle(n):
    global x, y
    global astre
    astre[n] = can.create_oval(x[n], y[n], x[n]+30, y[n]+30, fill='green')


astre = [1, 1]
fen = Tk()
can = Canvas(fen, width=300, height=300, bg='dark grey')
can.pack()
x = [160, 130]
y = [160, 130]
Button(fen, text='Oval1', command=cercle(0)).pack(side=BOTTOM)
Button(fen, text='Oval2', command=cercle(1)).pack(side=BOTTOM)

Button(fen, text='Quitter', command=fen.quit).pack(side=BOTTOM)


Button(fen, text='>', command=depl_droite1).pack(side=RIGHT)
Button(fen, text='^', command=depl_haut1).pack(side=RIGHT)
Button(fen, text='v', command=depl_bas1).pack(side=RIGHT)
Button(fen, text='<', command=depl_gauche1).pack(side=RIGHT)

Button(fen, text='<', command=depl_gauche2).pack(side=LEFT)
Button(fen, text='^', command=depl_haut2).pack(side=LEFT)
Button(fen, text='v', command=depl_bas2).pack(side=LEFT)
Button(fen, text='>', command=depl_droite2).pack(side=LEFT)


fen.mainloop()
