a=input("Enter a certain number of seconds")                       #entrer le nombre de secondes voulu
a=int(a)                                                           #convertir ce qui est entré en entier

secs=a%60                                                           #le reste de la division par 60 donne les secondes
minu=(a//60)%60                                                     #d'abord division entière par le nombre de secondes en une minute et ensuite reste par 60 pour trouver les minutes
hrs=(a//3600)%24                                                     #division entière par le nombre de secondes en une heure et ensuite reste par 24 pour trouver les heures
jrs=(a//86400)%30                                                   #division entière par le nombre de secondes en un jour et ensuite reste par 30 pour trouver les jours
mois=(a//2592000)%12                                            #division entière par le nombre de secondes en un mois et ensuite reste par 12 pour trouver les mois
yrs=a//31104000                                                 #division entière par le nombre de secondes en un an

print("{} annees {} mois {} jours {} heures {} minutes {} secondes".format(yrs,mois,jrs,hrs,minu,secs))