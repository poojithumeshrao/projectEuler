import math


f = open("p42.txt")
z = f.read()
a = z.split(',')


cnt = 0

for k in a:
    t = k[1:-1]
    s = 0
    for i in t:
        s+= ord(i) - 64

    d = math.sqrt(1+8*s)

    if d == int(d) and d%2 == 1:
        cnt+=1
print(cnt)
