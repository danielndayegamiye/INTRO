
def nomMois(an):
    "une fonction qui renvoie le nom du énième mois de l’année"
    mois=[1,"Janvier",2,"Fevrier",3,"Mars",4,"Avril",5,"Mai",6,"Juin",7,"Juillet",8,"Aout",9,"Septembre",10,"Octobre",11,"Novembre",12,"Décembre"]
    i=0
    while i<len(mois):
        if an == mois[i]:
            t=mois[i+1]
        i+=1
    return t

an=input("entrez le nième mois que vous voulez connaitre :")
an=int(an)
t=nomMois(an)
print("Le mois de : {}".format(t))