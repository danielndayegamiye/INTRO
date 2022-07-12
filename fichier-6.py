# un script qui permette d’encoder un fichier texte dont les lignes contiendront chacune
# les noms, prénom, adresse, code postal et no de téléphone de différentes personnes

try:
    f = open("monfichier6", "a")
except FileNotFoundError:
    f = open("monfichier6", "w")

while 1:
    i = 0
    liste = []
    nom = input("Nom: ")
    if nom == "":
        break
    prenom = input("Prenom: ")
    adresse = input("Adresse: ")
    code = input("Code Postal: ")
    num = input("Téléphone: ")
    liste += [nom, prenom, adresse, code, num]
    while i < len(liste):
        f.write(liste[i] + " ")
        i += 1
    f.write("\n")

f.close()
f = open("monfichier6", "r")
r = f.readlines()
print(r)
f.close()
