
from tkinter import*
c1 = 'red'
c2 = 'green'
a = None


def change():
    global c1, c2, a
    a = c1
    c1 = c2
    c2 = a
    can.create_oval(40, 60, 50, 70, fill=c2)
    can.create_oval(40, 140, 50, 150, fill=c1)
    can.create_oval(150, 60, 160, 70, fill=c1)
    can.create_oval(150, 140, 160, 150, fill=c2)


i = 0
fen = Tk()
can = Canvas(fen, width=200, height=240, bg='white')
can.pack()
ov = can.create_rectangle(50, 0, 150, 240, fill='dark grey')
x = 50
while i < 7:
    can.create_rectangle(x, 70, x+10, 140, fill='yellow')
    x += 15
    i += 1
Button(fen, text='feux', command=change).pack()
fen.mainloop()
