from tkinter import *


class Application(Frame):
    def __init__(self, boss=None):
        Frame.__init__(self)
        self.can = Canvas(self, width=400, height=400, bg='black')
        self.can.pack(padx=20, pady=10)
        Button(self, text='OUVRIR', command=self.ouvrir).pack(side=LEFT, padx=5, pady=5)
        Button(self, text='FERMER', command=self.fermer).pack(side=RIGHT, padx=5, pady=5)
        Button(self, text='QUITTER', command=self.quit).pack(side=BOTTOM)


class Visage(Application):
    def __init__(self, boss=None):
        Application.__init__(self)
        self.t = self.cercle(200, 200, 150)
        self.o1 = self.cercle(120, 120, 30, 'red')
        self.o2 = self.cercle(280, 120, 30, 'red')
        self.o = self.cercle(200, 250, 40, 'yellow')

    def cercle(self, x, y, r, col='white'):
        return self.can.create_oval(x-r, y-r, x+r, y+r, fill=col)

    def ouvrir(self):
        self.can.delete(self.o)
        self.o = self.cercle(200, 250, 40, 'yellow')

    def fermer(self):
        self.can.delete(self.o)
        self.o = self.can.create_line(150, 250, 250, 250)


if __name__ == '__main__':
    root = Tk()
    c = Visage(root)
    c.pack()
    root.mainloop()
