#pgme calculant le nombre de notes entrées,la note la plus élevée,la note la plus basse,la moyenne de toutes les notes

notes=1
t1=[]
i=0
som=0

while notes > 0:
    notes=input("Entrez la note :")
    notes=int(notes)
    if notes <0:
        break
    i+=1
    som+=notes
    moy= som/i
    t1.append(notes)
    a = 0
    maxi=0
    mini=1000000


    while a< len(t1):
        if t1[a] >maxi:
            maxi=t1[a]
        if t1[a]<= mini:
            mini=t1[a]
        a+=1
    print("le nombre de notes entrées :{} ,la note la plus élevée :{} ,la note la plus basse :{} ,la moyenne de toutes les notes :{}".format(i,maxi,mini,moy))

print("notes :{}".format(t1))
