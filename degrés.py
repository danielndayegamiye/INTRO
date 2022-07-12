#programme traduisant les radians en degrés

from math import pi

rad=input("entrer l'angle en radians:")
rad=float(rad)

a=(rad*180/pi)*3600
sec=int((a/3600)%3600)
min=int((a/60)%60)
deg=int(a//3600)

print("{} degrés {} minutes {} secondes".format(deg,min,sec))
