#pgme differenciant les nombres pairs des nombres impairs dans une liste

a=[32, 5, 12, 8, 3, 75, 2, 15]
pa=[]
imp=[]
i=0

while i< len(a):
    if a[i] %2 ==0:
        pa.append(a[i])
    else:
        imp.append(a[i])
    i+=1

print("pair :{} \nimpair :{}".format(pa,imp))