def po(a):
    p= 1
    for i in range(a):
        p*=a
        p%=10000000000
    return p

s=0
for i in range(1,1001):
    s+=po(i)
    s%=10000000000

print(s)
