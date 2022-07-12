def compteMots (ch):
    "une fonction qui renvoie le nombre de mots contenus dans la phrase"
    t= len(ch.split())
    return t


ch= input("entrez une phrase :")
print("Il y a {} mots".format(compteMots(ch)))