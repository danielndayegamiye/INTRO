class JeuDeCartes(object):
    def __init__(self):
        self.liste = [(2, 3), (3, 3), (4, 3), (5, 3), (6, 3), (7, 3), (8, 3), (9, 3), (10, 3), (11, 3),
                      (12, 3), (13, 3), (14, 3), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2), (8, 2),
                      (9, 2), (10, 2), (11, 2), (12, 2), (13, 2), (14, 2), (2, 1), (3, 1), (4, 1), (5, 1),
                      (6, 1), (7, 1), (8, 1), (9, 1), (10, 1), (11, 1), (12, 1), (13, 1), (14, 1), (2, 0),
                      (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0), (9, 0), (10, 0), (11, 0), (12, 0),
                      (13, 0), (14, 0)]
        self.liste1 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        self.liste2 = [3, 2, 1, 0]

    def nom_carte(self, t=(0, 1)):
        self.t = t
        if self.t[0] not in self.liste1 or self.t[1] not in self.liste2:
            return 'Erreur'
        dic1 = {14: 'As', 13: 'Roi', 12: 'Dame', 11: 'Valet'}
        dic2 = {0: 'Coeur', 1: 'Carreau', 2: 'Trèfle', 3: 'Pique'}
        if self.t[0] in dic1.keys():
            n1 = dic1[self.t[0]]
        else:
            n1 = self.t[0]
        n2 = dic2[self.t[1]]
        return '{} de {}'.format(n1, n2)

    def battre(self):
        import random
        random.shuffle(self.liste)

    def tirer(self):
        t = len(self.liste)
        if t > 0:
            carte = self.liste[0]
            del (self.liste[0])
            return carte
        else:
            return None


if __name__ == '__main__':
    jeuA = JeuDeCartes()
    jeuB = JeuDeCartes()
    jeuA.battre()
    jeuB.battre()
    pointA = 0
    pointB = 0
    for n in range(52):
        c = jeuA.tirer()
        d = jeuB.tirer()
        if c[0] > d[0]:
            pointA += 1
        elif d[0] > c[0]:
            pointB += 1
    if pointA > pointB:
        print("Le gagnant, c'est A avec: {}".format(pointA))
    elif pointB > pointA:
        print("Le gagnant, c'est B avec: {}".format(pointB))
