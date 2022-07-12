#pgme qui relie un mois par le nombre de jours qui le composent

i=0
t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
t2 = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin','Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']

res=[]

while i< len(t1):
    res.append(t2[i])
    res.append(t1[i])
    i+=1

print(res)