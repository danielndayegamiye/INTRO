# un script qui recopie le fichier utilisé dans l’exercice précédent(fichier-6), en y ajoutant la date
# de naissance et le sexe des personnes

f = open("monfichier6", "r")
try:
    g = open("monfichier7", "a")
except FileNotFoundError:
    g = open("monfichier7", "w")

while 1:
    i = 0
    r = f.readline()
    if r == "":
        break
    a = r.split()
    print(a[1])
    date = input("Date de naissance: ")
    sexe = input("sexe: ")
    a.append(date)
    a.append(sexe)
    while i < len(a):
        g.write(a[i] + "   ")
        i += 1
    g.write("\n")
f.close()
g.close()
