from oscillo import *
from curseurs import *


class ShowVibra(Frame):
    """Démonstration de mouvements vibratoires harmoniques"""
    def __init__(self, boss=None):
        Frame.__init__(self)  # constructeur de la classe parente
        self.couleur = ['purple', 'yellow', 'orange', 'blue']
        self.trace = [0]*4  # liste des tracés (courbes à dessiner)
        self.controle = [0]*4  # liste des panneaux de contrôle

        # Instanciation du canevas avec axes X et Y :
        self.gra = OscilloGraphe(self, larg=400, haut=200)
        self.gra.configure(bg='grey', bd=2, relief=SOLID)
        self.gra.pack(side=TOP, pady=5)

        # Instanciation de 4 panneaux de contrôle (curseurs) :
        for a in range(4):
            self.controle[a] = ChoixVibra(self, self.couleur[a])
            self.controle[a].pack()

        # Désignation de l'événement qui déclenche l'affichage des tracés :
        self.master.bind('<Control-Z>', self.montreCourbes)
        self.master.title('Mouvements vibratoires harmoniques')
        self.pack()

    def valeurs(self, i):
        return self.controle[i].freq,self.controle[i].phase,self.controle[i].ampl,

    def montreCourbes(self, event):
        """(Ré)Affichage des trois graphiques élongation/temps"""
        for i in range(4):
            self.gra.delete(self.trace[i])
            freq, phase, ampl = self.valeurs(i)
            # Ensuite, dessiner le nouveau tracé :
            if self.controle[i].chk.get():
                self.trace[i] = self.gra.traceCourbe(freq, phase, ampl, self.couleur[i],)

# Code pour tester la classe : ###


if __name__ == '__main__':
    ShowVibra().mainloop()
