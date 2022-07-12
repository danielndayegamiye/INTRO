#programme de multiplication par 7 différenciant ceux qui sont multiples de 3 par*

i=1

while(i<=20):
    mult=i*7
    if (mult%3==0):
        print("{}*".format(mult))
    else:
        print(mult)
    i+=1