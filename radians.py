#programme traduisant les degrés en radians
from math import pi            #introduction de la valeur pi dans le programme
deg=input("entrer les degrés:")
mn=input("entrer les minutes:")
sec=input("entrer les secondes:")
deg=float(deg)
mn=float(mn)
sec=float(sec)

a=deg+(mn/60.0)+(sec/3600.0)           #transformation des minutes en degrés
b= a*pi/180

print("{} radians".format(b))