# un script qui compare les contenus de deux fichiers et signale la première différence
# rencontrée.
f = open("monfichier4", "r")
g = open("monfichier5", "r")


while 1:
    re = f.read(1)
    ad = g.read(1)
    if re != ad:
        print("Première différence:" + re + " ET " + ad)
        break

f.close()
g.close()
