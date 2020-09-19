nxt = {1:2,2:3,3:5,5:7,7:9,9:1}
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


def next(i):
    a = list(str(i))[::-1]

    c = -1
    #pdb.set_trace()
    for j in a:
        c+=1
        a[c] = str(nxt[int(j)])
        if j != '9':
            break
        if c == len(a)-1:
            a.append('1')
            break

    return int(''.join(a[::-1]))

j=1
cnt = 0
while j < 1000000:
    f=0
    ff = 0
    p=j
    if j==3:
        #pdb.set_trace()
        pass
    for k in range(len(list(str(j)))):
        #print(p)
        if not isPrime(p):
            f=1
            break
        if len(list(str(p))[1:]) != 0:
                p=int(''.join(list(str(p))[1:]))

    p=j
    if f != 1:
            for k in range(len(list(str(j)))):
                    #print(p)
                    if not isPrime(p):
                            ff=1
                            break
                    if len(list(str(p))[1:]) != 0:
                            p=int(''.join(list(str(p))[:-1]))
    if f == 0 and ff == 0:
        cnt+=j
        print(j)
    j=next(j)
print(cnt-17)
    
    
