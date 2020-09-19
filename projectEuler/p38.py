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
for a in range(9999,1,-1):
    if pan(a):
        if a== 9723:
            pdb.set_trace()
            pass
        ltt = []
        for b in range(1,9):
            if pan(b):
                t = a*b
                if not pan(t):
                    break
                ltt = ltt + list(str(t))
                if not pan(int(''.join(ltt))):
                    break
                if len(ltt) == 9:
                    print(a,ltt)
                    break

