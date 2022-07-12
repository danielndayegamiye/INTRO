# programme qui fait apparaître une fenêtre avec deux champs :
# l’un indique une température en degrés Celsius, et l’autre la même température exprimée en degrés Fahrenheit.
from tkinter import *


def ent(event):
    tc = float(entr1.get())
    tf = float(entr2.get())
    if tf == 0:
        entr2.delete(0)
        tf = tc*1.80+32.0
        entr2.insert(1, tf)
    elif tc == 0:
        entr1.delete(0)
        tc = (tf-32.0)/1.80
        entr1.insert(1, tc)


def eff():
    entr1.delete(0, 'end')
    entr2.delete(0, 'end')
    entr1.insert(0, 0)
    entr2.insert(0, 0)


fen1 = Tk()
txt1 = Label(fen1, text='celsius :')
txt2 = Label(fen1, text='farhneit :')
entr1 = Entry(fen1)
entr2 = Entry(fen1)
txt1.grid(row=0)
txt2.grid(row=1)
entr1.grid(row=0, column=1, sticky=E)
entr2.grid(row=1, column=1, sticky=E)
entr1.insert(1, 0)
entr2.insert(1, 0)
Button(fen1, text='effacer', command=eff).grid(column=1, sticky=S)
entr1.bind('<Return>', ent)
entr2.bind('<Return>', ent)


fen1.mainloop()
