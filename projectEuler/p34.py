factorial = {0:1,1:1,2:2,3:6,4:24,5:120,6:720,7:5040,8:40320,9:362880}

import pdb

a = 10

def sof(a):
    s = 0
    for i in list(str(a)):
       s+=factorial[int(i)]

    return s

def next(b):
    a=b
    if a==90:
        #pdb.set_trace()
        pass
    if a>sof(a):
        return a+1
    else:
        f = 0
        c = -1
        v = list(str(a))[::-1]
        for i in v:
            c += 1
            if f == 1:
                if int(i) != 9:
                    v[c] = str(int(i)+1)
                    break
                else:
                    v[c] = str(int(0))
                    if c+1 == len(v):
                        v.append('1')
                        break
            else:
                v[c] = str(int(0))
                f = 1

    return int(''.join(v[::-1]))

p = 10
while True:
    if p == sof(p):
        print(p)
    p=next(p)
    
