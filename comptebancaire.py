class CompteBancaire(object):
    def __init__(self, nom="Dupont", solde=1000):
        self.nom = nom
        self.solde = solde

    def depot(self, somme):
        self.solde += somme

    def retrait(self, somme):
        self.solde -= somme

    def affiche(self):
        print("Le solde du compte bancaire de {} est de {} euros.".format(self.nom, self.solde))


class CompteEpargne(CompteBancaire):
    def __init__(self, nom="Dupont", solde=1000):
        CompteBancaire.__init__(self)
        self.taux = 0.3
        self.nom = nom
        self.solde = solde

    def changetaux(self, taux=0.3):
        self.taux = taux

    def capitalisation(self, nbremois=1):
        self.nbreMois = nbremois
        self.solde += self.solde * self.taux * self.nbreMois / 100
        print("Capitalisation sur {} mois au taux mensuel de {} %.".format(self.nbreMois, self.taux))


if __name__ == '__main__':
    c1 = CompteEpargne('Duvivier', 600)
    c1.depot(350)
    c1.affiche()
    c1.capitalisation(12)
    c1.affiche()
    c1.changetaux(.5)
    c1.capitalisation(12)
    c1.affiche()
