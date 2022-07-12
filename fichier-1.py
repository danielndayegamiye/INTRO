
maxi = 0
i = 0
s = 0
f = open('monfichier', 'r')
r = f.readlines()
while i < len(r):
    if len(r[i]) >= maxi:
        maxi = len(r[i])
        s = i

    i += 1
print(r[s])
f.close()
