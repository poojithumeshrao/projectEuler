def ncr(n,r):
    if r == 0:
        return 1
    if n-r < r:
        r = n-r
    prod = 1
    for i in range(n-r+1,n+1):
        prod *= i
    for i in range(1,r+1):
        prod /= i
    return prod

cnt = 0
for n in range(10,101):
    for r in range(n):
        nc = ncr(n,r)
        if nc > 1000000:
            cnt += 1

print(cnt)
