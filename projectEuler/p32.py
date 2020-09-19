import pdb

def pan(a):
    c = len(list(str(a)))
    d = len(set(str(a)))
    if c == d and '0' not in list(str(a)):
        return True
    else:
        return False

#pdb.set_trace()
lt = []
for a in range(1,10000):
    if pan(a):
        for b in range(1,10000):
            if pan(b):
                t = a*b
                if len(list(str(a)) + list(str(b)) + list(str(t))) > 9:
                    break
                if pan(t):
                    if len(set(list(str(a)) + list(str(b)) + list(str(t)))) == 9:
                        if t not in lt:
                            lt.append(t)
                            print(a,b,t)


print(sum(lt))
