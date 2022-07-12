#pgme additionnant les multiples de 3 et de 5 se trouvant entre ces nombres

b=32
a=0
t=0
o=0

while a<b:
    if (b%3==0) and (b%5==0):
        t += b
    if (b%3==0) or (b%5==0):
        o += b
    b-=1

print("Addition des nombres multiples de 3 et de 5 se trouvant dans l'intervalle de{} à {} : {}".format(a,b,t))
print("Addition des nombres multiples de 3 ou de 5 se trouvant dans l'intervalle de{} à {} : {}".format(a,b,o))