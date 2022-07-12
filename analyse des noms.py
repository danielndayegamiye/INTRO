#pgme analysant une liste de noms si il a plus de six caractères ou non

nom=['Jean', 'Maximilien', 'Brigitte', 'Sonia', 'Jean-Pierre', 'Sandra']
i=0
car=[]
plus_car=[]

while i< len(nom):
    if len(nom[i]) <6:
        car.append(nom[i])
    else:
        plus_car.append(nom[i])
    i+=1

print("moins de 6 caractères :{}\n6 caractères et plus :{}".format(car,plus_car))