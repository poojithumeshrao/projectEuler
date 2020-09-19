import pdb

currency = [1,2,5,10,20,50,100,200]
current = [200,0,0,0,0,0,0,0]


def total():
    t= 0;
    for i in range(len(currency)):
        t+=currency[i]*current[i]
    return t

#print(total())
tt = 10
cnt = 0
i=0
'''
def rec(i):
    #pdb.set_trace()
    #print(i)
    if i>=len(current) or i<0:
        #print(i)
        return
    global cnt
    if total()==tt:
        cnt+=1
        print(current)
    if (current[i] * currency[i]) > currency[i+1]  and total()<=tt:
        current[i]-=1
        current[i+1]+=1
        rec(i+1)
    if total()>tt:
        current[i]-=1
        rec(i-1)
    if (current[i] * currency[i]) < currency[i+1]:
        rec(i-1)
        
rec(0)
        
        
'''

queue=[]
lst = []

queue.insert(0,current)


i=0
#pdb.set_trace()
while len(queue)>0:
    for j in range(i+1,len(currency)):
        temp = queue[-1].copy()
        temp[i] = temp[i]*currency[i] - currency[j]
        temp[j] += 1
        if temp[i] >= 0:
            if temp not in lst:
                lst.insert(0,temp)
                queue.insert(0,temp)
                print(temp)
    queue.pop()
print(len(lst))
        
