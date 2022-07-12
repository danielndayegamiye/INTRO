# recherche occurence de lettres dans le fichier

al = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
      'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
      'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
      'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

dic = {}

for car in al:
    dic[car] = 0

f = open('dic1', 'r')
while 1:
    car = f.read(1)
    if car == '':
        break
    if car in dic.keys():
        dic[car] += 1

for cle in dic.keys():
    if dic[cle] != 0:
        print(cle, dic[cle], end=' ; ')

f.close()

# recherche ocurence de mots dans le fichier
f = open('dic1', 'r')
print("\n")
mots = f.read()
s = ''

for car in mots:
    if car in ',;:!':
        car = ' '
    s += car  # creation d'une nouvelle chaine les caractères virgules remplacés par des espaces
    # pour l'utilisation de split

mots = s.split()
dic1 = {}

for mot in mots:
    if mot in dic1.keys():
        dic1[mot] += 1
    else:
        dic1[mot] = 1


for cle in dic1.keys():
    print(cle, dic1[cle], end=' ; ')

# cette partie en bas est floue elle concerne la recherche de la position d'un mot dans le fichier
dic2 = {}
a = 0
i = 0
for mot in mots:
    dic2[mot] = []
for mot in mots:      # i+=5 pour qu'il ne ramene pas la position du précédent,
    # cela implique que chaque mot doit avoir au moins 5 lettres
    a = s.find(mot, i)
    dic2[mot].append(a)
    i += 5

for cle in dic2.keys():
    print(cle, dic2[cle])

f.close()
