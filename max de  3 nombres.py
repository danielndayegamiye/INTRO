#pgme renvoyant le plus grand de 3 nombres

def maximum (n1,n2,n3):
    maxi= max(n1,n2,n3)
    return maxi

a,b,c= eval(input("entrez 3 nombres : "))

maxi=maximum(a,b,c)

print("Le plus grand c'est: {}".format(maxi))



