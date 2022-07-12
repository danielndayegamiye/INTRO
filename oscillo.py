from tkinter import *
from math import sin, pi


class OscilloGraphe(Canvas):
    "Canevas spécialisé, pour dessiner des courbes élongation/temps"
    def __init__(self, boss=None, larg=300, haut=200):
        "Constructeur du graphique : axes et échelle horiz."
        # construction du widget parent :
        Canvas.__init__(self)  # appel au constructeur
        self.configure(width=larg, height=haut)  # de la classe parente
        self.larg, self.haut = larg, haut  # mémorisation
        # tracé d'une échelle avec 8 graduations :
        pas = (larg-25)/8.  # intervalles de l'échelle horizontale
        pas2 = (haut - 41) / 10
        for t in range(0, 9):
            stx = 10 + t*pas  # +10 pour partir de l'origine
            self.create_line(stx, 5+pas2, stx, 5+11*pas2, fill='dark green')

        for t in range(1, 12):
            sty = 5 + t*pas2
            self.create_line(10, sty, stx, sty,fill='dark green')
        # tracé des axes de référence :
        self.create_line(10, haut / 2, larg, haut / 2, arrow=LAST)  # axe X
        self.create_text((larg + 15) / 2, 10, text='e')
        self.create_line((larg - 5) / 2, haut - 5, (larg - 5) / 2, 5, arrow=LAST)  # axe Y
        self.create_text(larg - 10, haut / 2 - 15, text='t')

    def traceCourbe(self, freq=1, phase=0.0, ampl=10, coul='red'):
        "tracé d'un graphique élongation/temps sur 1 seconde"
        curve = []  # liste des coordonnées
        pas = (self.larg-25)/1000  # l'échelle X correspond à 1 seconde
        for t in range(0, 1001, 5):
            e = ampl*sin(2*pi*freq*t/1000 - phase)
            x = 10 + t*pas
            y = self.haut/2 - e*self.haut/30
            curve.append((x, y))
        n = self.create_line(curve, fill=coul, smooth=1)
        return n  # n = numéro d'ordre du tracé

#### Code pour tester la classe : ####


if __name__ == '__main__':
    root = Tk()
    g1 = OscilloGraphe()
    g1.pack()

    root.mainloop()
