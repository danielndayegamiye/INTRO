dic = {}
dic_rec = {}


def en():
    """ pour l'enregistrement dans le fichier"""
    try:
        f = open("dic2", "a")
    except FileNotFoundError:
        f = open("dic2", "w")
    for name in dic.keys():
        f.write(name+"@"+dic[name][0]+"#"+dic[name][1]+"\n")

    f.close()


def rec():
    """ pour la récupération des données dans le fichier"""
    try:
        f = open("dic2", "r")
    except FileNotFoundError:
        print("pas de dictionnaire préexistant")
    nom = []
    age = []
    taille = []
    r = f.readlines()
    f.close()
    f = open("dic2", "r")
    i = 0
    while i < len(r):
        s = ''
        lec = f.readline()
        for ca in lec:

            if ca == '@':
                nom.append(s)
                s = ''
            elif ca == '#':
                age.append(s[1:])
                s = ""
            elif ca == "\n":
                taille.append(s[1:])
            s += ca

        i += 1
    f.close()
    val = list(zip(age, taille))
    a = 0

    while a < len(nom):
        dic_rec[nom[a]] = val[a]
        a += 1
    return dic_rec


def remp():
    """la première pour le remplissage du dictionnaire"""

    while 1:
        nom = input("Entrez votre nom : ")
        if nom == "":
            return dic, en()
        age = input("Entrez votre age : ")
        taille = input("Entrez votre taille en mètres : ")
        dic[nom] = (age, taille)


def cons():
    """ la seconde pour sa consultation."""
    rec()
    nom = input("Entrez le nom à rechercher :")
    if nom in dic_rec:
        print("NOM : {} \t-age : {} \t--taille : {}".format(nom, dic_rec[nom][0], dic_rec[nom][1]))
    else:
        print("PAS DANS LE DICTIONNAIRE")


def quitter():
    global flag
    flag = 0
    return flag


flag = 1

while flag:
    print()
    c = input("1.Remplir le dictionnaire\t2.Consulter le dictionnaire\t3.Quitter  :")
    c = int(c)
    if c == 1:
        remp()
    elif c == 2:
        cons()
    else:
        quitter()
