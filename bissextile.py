#pgme vérifiant qu'une année est bissextile

an=input("Entrez l'année :")
an=int(an)

if (an%4 ==0) and (an%100!=0):
    print("ANNEE BISSEXTILE")
elif (an%400 ==0):
    print("ANNEE BISSEXTILE")
else:
    print("ANNEE NON BISSEXTILE")