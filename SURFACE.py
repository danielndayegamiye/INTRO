#pgme doit renvoyer la surface (l’aire) d’un cercle dont on lui a fourni le rayon R en argument.

from math import pi

def SurfCercle(R):
    "fonction calculant l'aire d'un cercle"
    aire = R*R*pi
    return aire

r=input("Entrez le rayon :")
r=int(r)
aire= SurfCercle(r)
print("L'aire est de: {}".format(aire))


