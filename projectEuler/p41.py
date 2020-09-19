import pdb
def pan(a):
    aa = list(str(a))
    if '0' in aa:
        return False
    c = len(aa)
    d = len(set(aa))
    if c == d  and int(max(aa)) == c:
        return True
    else:
        return False

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
for i in range (999999999,2,-2):
    #pdb.set_trace()
    if i%5 != 0 and i%3 != 0 and i%7 != 0 and pan(i):
        print(i)
        if isPrime(i):
            break
    
        


