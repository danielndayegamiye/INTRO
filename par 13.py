#programme de multiplication par 13 montrant uniquement ceux qui sont multiples de 7

i=1

while(i<=50):
    mult=i*13
    if (mult % 7 == 0):
        print(mult)
    i+=1