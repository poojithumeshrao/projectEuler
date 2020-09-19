i=1023456799
cnt = 0

def pan(a):
    c = len(list(str(a)))
    d = len(set(str(a)))
    if c == d:
        return True
    else:
        return False



while i< 9087654321:
    a = int(i/1000000)
    b = int(i/100000)
    c = int(i/10000)
    d = int(i/1000)
    e = int(i/100)
    f = int(i/10)
    if a%1000%2 != 0:
        i=a*1000000
        i+=1000000*(2-a%1000%2)
    elif b%1000%3 != 0:
        i=b*100000
        i+=100000*(3-b%1000%3)
    elif c%1000%5 !=0:
        i=c*10000
        i+=10000*(5-c%1000%5)
    elif d%1000%7 != 0:
        i=d*1000
        i+=1000*(7-d%1000%7)
    elif e%1000%11 != 0:
        i=e*100
        i+=100*(11-e%1000%11)
    elif f%1000%13 != 0:
        i=f*10
        i+=10*(13-f%1000%13)
    elif i%1000%17 != 0:
        i+=17-i%1000%17
    else:
        if pan(i):
            print(i)
            cnt+=i
        i+=1
print(cnt)
