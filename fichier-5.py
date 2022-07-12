# À partir de deux fichiers préexistants A et B, construisez un fichier C qui contienne
# alternativement un élément de A, un élément de B, un élément de A... et ainsi de suite jusqu’à
# atteindre la fin de l’un des deux fichiers originaux.
f = open("monfichier4", "r")
g = open("monfichier5", "r")
new = open("monfichier6", "w")

while 1:
    re = f.read(1)
    ad = g.read(1)
    new.write(re)
    new.write(ad)
    if re == "" and ad == "":
        break


new.close()
f.close()
g.close()
new = open("monfichier6", "r")
r = new.readline()
print(r)
new.close()
