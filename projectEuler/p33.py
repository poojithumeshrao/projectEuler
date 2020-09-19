for a in range(10,100):
    for b in range(a,100):
        t1=list(str(a))
        t2=list(str(b))
        #print(t1,t2)
        if t1[0]==t2[1]:
            del t1[0]
            del t2[1]
            aa = int(''.join(t1))
            bb = int(''.join(t2))
        elif t1[1] == t2[0]:
            del t1[1]
            del t2[0]
            aa = int(''.join(t1))
            bb = int(''.join(t2))
        else:
            continue

        if aa != 0 and a != 0 and b/a == bb/aa and a != b:
            print(a,b)
