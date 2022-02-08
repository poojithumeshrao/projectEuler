def period(arr):

    temp = []

    for a in arr:
        if len(temp) == 0:
            temp.append(a)
            continue

        else:

            for i in range(len(arr)):
                if arr[i] != temp[i%len(temp)]:
                    temp.append(a)
                    break

    return len(temp)


def vals(a,b,c):
    t = (a - b ** 2) / c

    d = int( ((a ** 0.5) - b) / t)

    b = -b - d * t

    return d,a,b,t

#print(period([1,2,4,3,1,2,4,3,1,2]))


cnt = 0

for i in range(2,10001):
    temp = []
    
    b,d = i,1

    print(i)
    if int(i ** 0.5) == i ** 0.5:
        continue

    c = -int(i ** 0.5)

    
    for j in range(500):
        a , b, c, d = vals(b,c,d)
        temp.append(a)
        #print(a,b,c,d)

    per = period(temp)

    if per > 400:
        print("temp")
        break
    if per % 2 != 0:
        cnt += 1


print(cnt)
    
