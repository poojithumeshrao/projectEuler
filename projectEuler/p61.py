def value(s,n):
    return ((s-2) * (n * (n-1)) / 2 ) + n

def check_comp(vals):
    flag = True
    cnt = 0
    for i in range(len(vals)):
        v = vals[i]
        f2 = False
        for j in range(len(vals)):
            v2 = vals[j]
            if v%100 == v2//100 and i!=j:
                f2 = True

        if f2 == False:
            cnt += 1
            flag = False

    return flag,cnt


def check_comp_2(vals):
    flag = True
    cnt = 0
    for i in range(len(vals)):
        v = vals[i]
        f2 = False
        for j in range(len(vals)):
            v2 = vals[j]
            if v//100 == v2%100 and i!=j:
                f2 = True

        if f2 == False:
            cnt += 1
            flag = False

    return flag,cnt

val_list = []
for s in range(3,9):
    s_l = []
    for i in range(500):
        val = value(s,i)
        if val > 999 and val < 10000:
            s_l.append(val)

    val_list.append(s_l)

cnt = 0
for v1 in val_list[0]:
    #print(v1)
    for v2 in val_list[1]:
        for v3 in val_list[2]:
            for v4 in val_list[3]:
                for v5 in val_list[4]:
                    for v6 in val_list[5]:
                        dec,cnt = check_comp([v1,v2,v3,v4,v5,v6])
                        if cnt > 3:
                            cnt -= 1
                            break
                        elif dec :
                            dec2,cnt2 = check_comp_2([v1,v2,v3,v4,v5,v6])
                            if dec2:
                                print(dec,[v1,v2,v3,v4,v5,v6],sum([v1,v2,v3,v4,v5,v6]))
                            cnt = max(cnt,cnt2)

                    if cnt > 3:
                        cnt -= 1
                        break
                if cnt > 3:
                    cnt -= 1
                    break
            if cnt > 3:
                cnt -= 1
                break
        if cnt > 3:
            cnt -= 1
            break
    if cnt > 3:
        cnt -= 1
        break



#print()
