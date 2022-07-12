# un programme dans lequel évoluent plusieurs balles de couleurs différentes, qui
# rebondissent les unes sur les autres ainsi que sur les parois.

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
    if x >= x1-25 and x <= (x1+c+25) and y >= y1-25 and y <= (y1+c+25):
        s = -s
        d = -d
    x += f
    y += d
    x1 += t
    y1 += s
    can.coords(ov, x, y, x+c, y+c)
    can.coords(ov1, x1, y1, x1+c, y1+c)
    if flag == 0:
        fen.after(v, move)


def stop():
    global flag
    flag = 1
    move()


fen = Tk()
can = Canvas(fen, width=400, height=250, bg='dark grey')
can.pack()
x = 20
y = x
x1 = 150
y1 = x1
c = 30
ov = can.create_oval(x, y, x+c, y+c, fill='orange')
ov1 = can.create_oval(x1, y1, x1+c, y1+c, fill='yellow')
f = 6
d = 5
t = 6
s = 5
flag = 0
po = 0
v = 30
a = 0
b = 0
Button(fen, text='Pause', command=stop).pack(side='bottom', padx=5, pady=5)
Button(fen, text='start', command=move).pack(side='bottom', pady=10)
Button(fen, text='Quitter', command=fen.quit).pack(side='right', pady=10)
fen.mainloop()
