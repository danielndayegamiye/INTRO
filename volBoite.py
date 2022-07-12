#pgme qui renvoie le volume d’une boîte parallélépipédique
def volBoite(x1=10,x2=10,x3=10):
    "fonction qui renvoie le volume d’une boîte parallélépipédique"
    vol= x1*x2*x3
    return vol
a,b,c= eval(input("entrez les 3 dimensions du parallelepipede :"))
vol=volBoite(a,b,c)

print("Le volume est de : {}".format(vol))