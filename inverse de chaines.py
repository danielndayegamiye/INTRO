#pgme inversant chaque mot que tu entres

ch=input("Entrez n'importe quel  mot :")
i= len(ch) -1
t=""

while i>=0:
    t += ch[i]
    i-=1

if t==ch :
    print("Cette chaine est un palindrome")                                    #cela veut dire que si tu inverse la chaine tu obtiens la meme chaine

print(t)