# Python3 program to check whether a number
# is prime or not using recursion

# Function check whether a number
# is prime or not

from math import sqrt

def isPrime(n):
	
    if (n <= 1):
        return False
 
    # Check from 2 to sqrt(n)
    for i in range(2, int(sqrt(n))+1):
        if (n % i == 0):
            return False
 
    return True

def perc(arr):
    cnt = 0
    for c in arr:
        if c:
            cnt += 1
    return cnt / len(arr)


diag = [1]
diag_prime = [False]
cur = 1
add_var = 2
len_side = 1
while True:
    for _ in range(4):
        cur += add_var 
        diag.append(cur)
        diag_prime.append(isPrime(cur))
    add_var += 2
    len_side += 2
    print(perc(diag_prime))
    if (perc(diag_prime) < 0.1):
        print(len_side)
        break
