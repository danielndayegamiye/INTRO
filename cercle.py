from tkinter import *


class Application(Frame):
    def __init__(self, boss=None):
        Frame.__init__(self)
        self.canvas = Canvas(self, height=300, width=300, bg='white')
        self.canvas.pack()
        self.x = 150
        self.y = 150
        self.r = 15
        self.cer = self.canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r,
                                           self.y + self.r, fill='grey')
        Scale(self, orient=HORIZONTAL, showvalue=0, from_=15, to=90, command=self.circle,
              length=150, label='Radius').pack()

    def circle(self, r):
        r = float(r)
        x = self.x
        y = self.y
        self.canvas.coords(self.cer, x-r, y-r, x+r, y+r)


if __name__ == '__main__':
    root = Tk()
    c = Application(root)
    c.pack()
    root.mainloop()
