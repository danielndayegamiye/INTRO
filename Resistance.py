class Application(object):
    def __init__(self):
        self.root = Tk()
        self.root.title('Code des couleurs')
        self.dessineresistance()
        Label(self.root, text="Entrez la valeur de la résistance").grid(row=2, column=1, columnspan=3)
        Button(self.root, text="Quittez", command=self.root.quit).grid(row=3, column=3)
        self.entree = Entry(self.root, width=14)
        self.entree.grid(row=3, column=1)
        self.root.bind("<Return>", self.changecouleurs)
        self.coul = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'grey', 'white']
        self.root.mainloop()

    def dessineresistance(self):
        self.can = Canvas(self.root, height=100, width=250, bg='ivory')
        self.can.grid(row=1, column=1, columnspan=3, pady=5, padx=5)
        self.can.create_line(10, 50, 240, 50, width=5)
        self.can.create_rectangle(65, 30, 185, 70, fill='light grey', width=2)
        self.liste = []
        for x in range(75, 165, 30):
            self.liste.append(self.can.create_rectangle(x, 30, x+12, 70, fill='black'))

    def changecouleurs(self, event):
        self.val = self.entree.get()
        err = 0
        v = 0
        li = [0] * 3
        try:
            v = float(self.val)
        except:
            err = 1
        if err == 1 or v > 1e11 or v < 0:
            for n in range(3):
                self.can.itemconfigure(self.liste[n], fill=self.coul[li[n]])
            self.erreur()

        elif v >= 0 and v < 10:
            li[0] = 0
            li[1] = int(v)
            decim = v-li[1]
            li[2] = int(decim*10 + 0.5)
            for n in range(3):
                self.can.itemconfigure(self.liste[n], fill=self.coul[li[n]])
        else:
            logv = log10(v)
            gd = int(logv)
            ec = 10**gd
            li[0] = int(v/ec)
            decim = v/ec - li[0]
            li[1] = int(decim*10 + 0.5)
            li[2] = gd - 1
            for n in range(3):
                self.can.itemconfigure(self.liste[n], fill=self.coul[li[n]])

    def erreur(self):
        self.entree.configure(bg='red')
        self.root.after(1000, self.vide)

    def vide(self):
        self.entree.configure(bg='white')
        self.entree.delete(0, len(self.val))


if __name__ == '__main__':
    from tkinter import *
    from math import log10
    f = Application()
