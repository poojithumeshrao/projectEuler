import math
import pdb


def pen(a):
    if int((1 + math.sqrt(1+24*a))/6) == (1 + math.sqrt(1+24*a))/6:
        return True
    else:
        return False



class pent:
    def __init__(self,start = 1):
        self.i = int((1 + math.sqrt(1+24*start))/6)

    def __iter__(self):
        return self
        
    def __next__(self):
        n = self.i*(3*self.i -1) / 2
        self.i+=1
        return int(n)

p = pent()
size = 100000000
for i in iter(p):
    q = pent(i)
    sz = 0
    cnt = 0
    for j in iter(q):
        cnt+=1
        #print(i,j)
        if i==22:
            #pdb.set_trace()
            pass
        if pen(i+j) and pen(j-i):
            size == min(size,j-i)
            print(i,j)
            print(size)
            break
        if cnt>1000000:
            break
        if j-i>size :
            break
