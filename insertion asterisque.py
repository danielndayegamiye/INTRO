#pgme inserant des asterisques entre les lettres

ch=input("Entrez n'importe quel  mot :")
i=0
t=""

while i<len(ch):
    t+=ch[i] + '*'
    i+=1

print(t)