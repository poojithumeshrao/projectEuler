import math
import pdb

def tri(a):
    if int((-1 + math.sqrt(1+8*a))/2) == (-1 + math.sqrt(1+8*a))/2:
        return True
    else:
        return False

def hex(a):
    if int((1 + math.sqrt(1+8*a))/4) == (1 + math.sqrt(1+8*a))/4:
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


c = 0
for a in iter(p):
    if tri(a) and hex(a):
        print(a)
    c+=1    
