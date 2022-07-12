p=2
i=1
f=open('monfichier2','w')
while p <= 30:
    while i <= 20:
        s=i*p
        f.write(str(p)+"*"+str(i)+"="+str(s))
        f.write("\n")
        i+=1
    f.write("\n\n\n")
    i=1
    p+=1

f.close()