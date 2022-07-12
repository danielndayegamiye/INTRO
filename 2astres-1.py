# pgme permettant de controler la position de 2 astres

from tkinter import *


def avance(event):
    global x, y, astre, a
    gd = event.x
    hb = event.y
    x[a] = gd
    y[a] = hb
    can.coords(astre[a], x[a], y[a], x[a]+30, y[a]+30)


def ov1():
    global a
    a = 0


def ov2():
    global a
    a = 1


astre = [""]*2
fen = Tk()
can = Canvas(fen, width=300, height=300, bg='dark grey')
can.bind("<Button-1>", avance)
can.pack()
x = [160, 130]
y = [160, 130]
n = 0
col = 'green'
while n <= 1:
    astre[n] = can.create_oval(x[n], y[n], x[n] + 30, y[n] + 30, fill=col)
    col = 'red'
    n += 1

a = 0
Label(fen, text="CLIQUE SUR UN DES BOUTONS POUR LES OVALES\n oval1=vert, oval2=rouge").pack()

Button(fen, text='Oval1', command=ov1).pack(side=BOTTOM)
Button(fen, text='Oval2', command=ov2).pack(side=BOTTOM)


Button(fen, text='Quitter', command=fen.quit).pack(side=BOTTOM)


fen.mainloop()
