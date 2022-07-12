#programme qui calcule lee nombre de fois qu'apparait 'e'

ch=input("Entrez n'importe quel  mot :")
i=0
t=0

while i<len(ch):
    if ch[i] == 'e':
        t+=1
    i+=1

print("'e' apparait {} fois".format(t))
