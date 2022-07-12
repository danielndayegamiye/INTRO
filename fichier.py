# un script qui permette de créer et de relire aisément un fichier texte


def choice():
    global f, filename
    ch = input("1.enregistrer de nouvelles lignes de texte\n2.d’afficher le contenu du fichier.")
    ch = int(ch)
    if ch == 1:
        f = open(filename, 'a')
        while 1:
            n = input()
            if n == "":
                break
            n = n + "\n"
            f.write(n)
        f.close()
    elif ch == 2:
        f = open(filename, 'r')
        while 1:
            r = f.readline()
            if r == "":
                break
            print(r)
        f.close()
    else:
        print("Mauvais choix\nVeuillez recommencer")
        choice()


filename = input("Veuillez entrer le nom du fichier : ")
try:
    f = open(filename, 'r')
    f.close()
    print("Fichier existant")
    choice()
except FileNotFoundError:
    f = open(filename, 'w')
    f.close()
    print("Fichier vide")
    choice()
