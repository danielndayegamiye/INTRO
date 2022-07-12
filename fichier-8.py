# vous disposez à présent d’un
# fichier(monfichier7) contenant les coordonnées d’un certain nombre de personnes. Écrivez un script qui
# permette d’extraire de ce fichier les lignes qui correspondent à un code postal bien déterminé.

f = open("monfichier7", "r")
re = f.readlines()
i = 0
code = input("Mot à rechercher : ")
o = False
while i < len(re):
    if code in re[i]:
        print(re[i])
        o = True
    i += 1
if o:
    print("Trouvé")
else:
    print("Pas dans le fichier")
f.close()
