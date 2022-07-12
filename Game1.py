# programme de jeu
# fonctionnant de la manière suivante : une balle se déplace au hasard sur un canevas, à vitesse
# faible. Le joueur doit essayer de cliquer sur cette balle à l’aide de la souris. S’il y arrive, il gagne
# un point, mais la balle se déplace désormais un peu plus vite, et ainsi de suite.

from tkinter import *


def move():
    global x, y, flag, f, ov, v, d, c
    if x <= 5 or x >= 370:
        f = -f
    elif y <= 5 or y >= 230:
        d = -d
    x += f
    y += d
    can.coords(ov, x, y, x+c, y+c)
    if flag == 0:
        fen.after(v, move)


def stop():
    global flag, po
    flag = 1
    Label(fen, text='points:'+str(po)).pack()
    move()


def point(event):
    global x, y, a, b, po, v, c
    a = event.x
    b = event.y
    if a >= x and b >= y and a <= (x+c) and b <= (y+c):
        po += 5
        v -= 10
        c -= 5
        move()


def resume():
    global flag, po, c
    flag = 0
    po = 0
    c = 50
    move()


fen = Tk()
can = Canvas(fen, width=400, height=250, bg='dark grey')
can.pack()
x = 20
y = x
c = 50
ov = can.create_oval(x, y, x+c, y+c, fill='green')
f = 6
d = 5
flag = 0
po = 0
v = 250
a = 0
b = 0
Button(fen, text='Pause', command=stop).pack(side='bottom', padx=5, pady=5)
Button(fen, text='start', command=move).pack(side='bottom', pady=10)
Button(fen, text='Quitter', command=fen.quit).pack(side='right', pady=10)
Button(fen, text='Restart', command=resume).pack(side='left', padx=15, pady=5)
can.bind('<Button-1>', point)
fen.mainloop()
