import math
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

i=9
while(True):
    f=0
    for j in range(i-2,1,-2):
        a = (i-j)/2
        if isPrime(j) and int(math.sqrt(a)) == math.sqrt(a) :
            #print(i,j,a)
            f=1
            break
    if f== 0 and not isPrime(i):
        print(i)
    i+=2
