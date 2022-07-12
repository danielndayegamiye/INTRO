def compteCar(ca,ch):
    i=0
    t=0
    while i<len(ch):
        if ch[i] == ca:
            t+=1
        i+=1
    return t

ch=input("entrez un mot :")
ca=input("entrez le caractère :")
t=compteCar(ca,ch)

print(t,"fois")