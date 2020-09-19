permut = []
import pdb

def isPrime(n) : 
  
    # Corner cases 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
  
    # This is checked so that we can skip  
    # middle five numbers in below loop 
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
  
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
  
    return True



def perm(a,b):
    #pdb.set_trace()
    if len(rem(a,b)) == 0:
        t = int(''.join([str(k) for k in b]))
        if isPrime(t):
            permut.append(t)
        return
    for e in rem(a,b):
        perm(a,b+[e])



def rem(aa,bb):
    t = aa[:]
    for i in bb:
        t.remove(i)
    return t


for i in range(1001,10000,2):
    if i%3!=0 and i%5!=0 and i%7!=0 and i%11!=0 and isPrime(i):
        permut = []
        perm(list(str(i)),[])
        temp = permut
        if i==2969:
            #pdb.set_trace()
            pass
        if temp != None and len(temp)>3:
            temp.sort()
            for q in temp:
                if q > 1000:
                    for w in temp:
                        if w > q:
                            if 2*w-q in temp:
                                print(q,w,2*w-q,w-q)
        
#print(permut)
