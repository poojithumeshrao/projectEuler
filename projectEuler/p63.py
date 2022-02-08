cnt = 0
for j in range(1,1000):
    for i in range(1,1000):
        a = str(j**i)
        #print(len(a), i)
        if len(a) == i:
            #print(i)
            #break
            cnt +=1

        if len(a) < i:
            print(i)
            break
print(cnt)
