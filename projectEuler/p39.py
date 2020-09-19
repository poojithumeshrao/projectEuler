import math


l = []
for i in range(1,999):
    for j in range(i,999):
        k = math.sqrt(i**2 + j**2)
        if k == int(k) and (i+j+k)<1000:
            l.append(i+j+k)

l.sort()
#print(l)


mx = 0
c = 1
aa = 1
for i in range(len(l)-1):
    if l[i] == l[i+1] :
        c+=1
        if c>mx:
            mx = max(mx,c)
            aa = l[i]
    else:
        c=1

print(aa)

