# Chaque
# fois que l’on clique sur le bouton, la balle doit avancer d’une petite distance vers la droite,
# jusqu’à ce qu’elle atteigne l’extrémité du canevas. Si l’on continue à cliquer, la balle doit alors
# revenir en arrière jusqu’à l’autre extrémité, et ainsi de suite.

from tkinter import *

t = None
f = 10


def avance():
    global x, y, astre
    global f, t
    if x == 0 or (x + 30) == 300:
        f = -f
    x += f
    can.coords(astre, x, y, x+30, y+30)


fen = Tk()
can = Canvas(fen, width=300, height=300, bg='dark grey')
can.pack()
x = 160
y = 160
astre = can.create_oval(x, y, x+30, y+30, fill='green')
Button(fen, text='Avancer', command=avance).pack()

fen.mainloop()
