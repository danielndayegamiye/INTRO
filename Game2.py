# Il s’agit à
# présent pour le joueur de cliquer seulement sur la balle rouge. Un clic erroné (sur une balle
# d’une autre couleur) lui fait perdre des points.

from tkinter import *


def move():
    global x, y, flag, f, ov, v, d, c, x1, y1, ov1, t, s
    if x <= 5 or x >= 370:
        f = -f
    elif y <= 5 or y >= 220:
        d = -d
    if x1 <= 5 or x1 >= 370:
        t = -t
    elif y1 <= 5 or y1 >= 220:
        s = -s
    if x >= x1 - 25 and x <= (x1 + c + 25) and y >= y1 - 25 and y <= (y1 + c + 25):
        s = -s
        d = -d
    x += f
    y += d
    x1 += t
    y1 += s
    can.coords(ov, x, y, x + c, y + c)
    can.coords(ov1, x1, y1, x1 + c, y1 + c)
    if flag == 0:
        fen.after(v, move)


def stop():
    global flag, po
    flag = 1
    Label(fen, text='points:'+str(po)).pack()
    move()


def point(event):
    global x, y, a, b, po, v, c, x1, y1
    a = event.x
    b = event.y
    if a >= x and b >= y and a <= (x+c) and b <= (y+c):
        po += 5
        v -= 10
        c -= 5
        move()
    elif a >= x1 and b >= y1 and a <= (x1 + c) and b <= (y1 + c):
        po -= 1
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
x1 = 150
y1 = x1
c = 50
ov = can.create_oval(x, y, x+c, y+c, fill='red')
ov1 = can.create_oval(x1, y1, x1+c, y1+c, fill='yellow')
f = 6
d = 5
t = 6
s = 5
flag = 0
po = 0
v = 100
a = 0
b = 0
Button(fen, text='Pause', command=stop).pack(side='bottom', padx=5, pady=5)
Button(fen, text='start', command=move).pack(side='bottom', pady=10)
Button(fen, text='Quitter', command=fen.quit).pack(side='right', pady=10)
Button(fen, text='Restart', command=resume).pack(side='left', padx=15, pady=5)
can.bind('<Button-1>', point)
fen.mainloop()
