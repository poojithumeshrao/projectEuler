i=100
while True:
    i+=1
    num = len(list(str(i)))
    num_6 = len(list(str(i*6)))
    if num != num_6:
        i = 10**num
        print(i)
        continue
    print(i)
    set_i = set(str(i))
    if set_i  ==  set(str(i*6)):
        if set_i  ==  set(str(i*5)):
            if set_i  ==  set(str(i*4)):
                if set_i  ==  set(str(i*3)):
                    if set_i  ==  set(str(i*2)):
                        print(i)
                        break
                    else:
                        continue
                else:
                    continue
            else:
                continue
        else:
            continue
    else:
        continue
   
