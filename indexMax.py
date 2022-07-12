def indexMax(liste,debut=0,fin=-1):
    "une fonction qui renvoie l’index de l’élément ayant la valeur la plus élevée dans la liste transmise en argument"
    if fin==-1:
        fin=len(liste)
    maxi=0
    t=0
    while debut< fin:
        if maxi< liste[debut]:
            maxi= liste[debut]
            t =debut
        debut+=1
    return maxi


liste=[10,2,3,40,55,2]
t=indexMax(liste)
print("plus grand indice :",t)
serie = [9, 3, 6, 1, 7, 5, 4, 8, 2]
print(indexMax(serie))
print(indexMax(serie, 2, 5))
print(indexMax(serie, 2))
print(indexMax(serie, fin =3, debut =1))

