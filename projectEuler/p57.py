def step(a,b):
    return b,2*b+a

def num_digs(a):
    return(len(str(a)))
a,b = 1,2

#for j in range(1,1000):
cnt = 0
for i in range(999):
    a,b = step(a,b)
    #print(a+b,b)
    if num_digs(a+b) > num_digs(b):
        cnt+=1
print(cnt)
        
