# un programme pour le jeu du serpent : un « serpent » (constitué en fait d’une courte
# ligne de carrés) se déplace sur le canevas dans l’une des 4 directions : droite, gauche, haut, bas.
# Le joueur peut à tout moment changer la direction suivie par le serpent à l’aide des touches
# fléchées du clavier. Sur le canevas se trouvent également des « proies » (des petits cercles fixes
# disposés au hasard). Il faut diriger le serpent de manière à ce qu’il « mange » les proies sans
# arriver en contact avec les bords du canevas. À chaque fois qu’une proie est mangée, le serpent
# s’allonge d’un carré, le joueur gagne un point, et une nouvelle proie apparaît ailleurs. La partie
# s’arrête lorsque le serpent touche l’une des parois, ou lorsqu’il a atteint une certaine taille.

from tkinter import *
from random import randrange


def avance():
    global x, y, sn, flag, v, gd, hb, po, op, i
    x += gd
    y += hb
    v += 3

    can.coords(sn, x, y, x + c, y + d)
    if x <= 5 or x >= 380 or y <= 7 or y >= 225:
        flag = 1
        while i < 1:
            Label(can, text='GAME OVER\n Point: ' + str(po)).pack()
            i += 1

    op = can.find_overlapping(can.coords(ov)[0], can.coords(ov)[1], can.coords(ov)[2], can.coords(ov)[3])
    if op == (1, 2):
        point()
    if flag == 0:
        fen.after(v, avance)


def depl_gauche1(event):
    global c, d, gd, hb
    c = 20
    d = 5
    gd = -5
    hb = 0
    avance()


def depl_droite1(event):
    global c, d, gd, hb
    c = 20
    d = 5
    gd = 5
    hb = 0
    avance()


def depl_haut1(event):
    global c, d, gd, hb
    c = 5
    d = 20
    gd = 0
    hb = -5
    avance()


def depl_bas1(event):
    global c, d, gd, hb
    c = 5
    d = 20
    gd = 0
    hb = 5
    avance()


def point():
    global x, y, x1, y1, c, d, po
    po += 10
    x1 = randrange(200)
    y1 = x1
    can.coords(ov, x1, y1, x1+7, y1+7)
    avance()


fen = Tk()
can = Canvas(fen, width=400, height=250, bg='dark grey')
can.pack()
x = 200
y = 120
c = 20
d = 5
v = 120
gd = None
hb = None
po = 0
op = None
flag = 0
i = 0
sn = can.create_rectangle(x, y, x+c, y+d, fill='green')
x1 = 150
y1 = 100
ov = can.create_oval(x1, y1, x1+7, y1+7, fill='black')
fen.bind('<Up>', depl_haut1)
fen.bind('<Down>', depl_bas1)
fen.bind('<Right>', depl_droite1)
fen.bind('<Left>', depl_gauche1)
Button(fen, text='Quitter', command=fen.quit).pack(side=BOTTOM)

fen.mainloop()
