phrase = "Ceci est une toute petite phrase."

def changeCar(ch,ca1,ca2,debut=0,fin= len(phrase)):
    i=0
    ph=""
    while i<len(phrase):
        if i>=debut and i<=fin and ch[i]==ca1:
            ph+=ca2
        else:
            ph+=ch[i]
        i+=1
    return ph


print(changeCar(phrase,"e","a"))
print(changeCar(phrase, ' ', '*'))
print(changeCar(phrase, ' ', '*', 8, 12))
print(changeCar(phrase, ' ', '*', 12))
print(changeCar(phrase, ' ', '*', fin = 12))
