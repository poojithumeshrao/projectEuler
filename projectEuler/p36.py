import pdb

def nt(a):
    #if a == 191:
        #pdb.set_trace()
    la = list(str(a))
    l = len(la) -1
    p = int(l/2)
    while True:
        if p < 0:
            la = ['0' for i in la]
            la[0]='1'
            la.append('1')
            break
        
        if int(la[p]) < 9:
            la[p] = str(int(la[p])+1)
            if  (l)/2 != p :
                la[-1-p] = str(int(la[-1-p])+1)
            break
        else:
            la = la[:p] + ['0' for ll  in la[p:-p]] + la[-p:]
            p-=1

    return int(''.join(la))


def pal(a):
    a = list(a)
    a=a[2:]
    b = a[::-1]
    if a == b:
        return True
    else:
        return False


a=0
cnt=0
while a<1000000:
    if pal(bin(a)):
        #print(a)
        cnt+=a
    a = nt(a)
print(cnt)
