from collections import defaultdict

def is_pal(a):
    if str(a) == str(a)[::-1]:
        return True
    else:
        return False

#print(is_pal(242))

lychrel = defaultdict(lambda: -1)

cal_list = []
for i in range(1,10001):
    if lychrel[i] == -1:
        #print(i)
        cal_list.append(i)
        
        for j in range(50):
            nxt_num = cal_list[-1] + int(str(cal_list[-1])[::-1])
            
            if is_pal(nxt_num) or lychrel[nxt_num] == 1:
                for num in cal_list:
                    lychrel[num] = 1
                
                break
            else:
                cal_list.append(nxt_num)
        #print(cal_list)
        cal_list = []

cnt = 0
for i in range(1,10001):
    if lychrel[i] == 1: cnt+=1
    #break
print(10000-cnt)
