import pdb

prime = []

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



i=2
pr=1

ll = 0
while True:
    c=0
    if isPrime(i):
        prime.append(i)
        c=1
    else:
        a=i
    
        for p in prime:
            if a%p == 0:
                c+=1
                while a%p == 0:
                    a = a/p
        if a!=1 :
            print('error')

    #pdb.set_trace()
    if pr==c:
        ll+=1
    else:
        ll=0
    #print(ll)
    if ll == 3 and i!=4 and c==4:
        print(i,c)
        #pdb.set_trace()
        break
    i+=1
    pr=c
                














    
