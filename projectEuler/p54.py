from collections import Counter

num_dict = {'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'T':10,'J':11,'Q':12,'K':13,'A':14}

def high_card(p1,p2):
    num_1 = [num_dict[card[0]] for card in p1]
    num_2 = [num_dict[card[0]] for card in p2]

    num_1 = sorted(num_1,reverse=True)
    num_2 = sorted(num_2,reverse = True)
    for i in range(5):
        if num_1[i] > num_2[i] :
            return 1
        elif num_1[i] < num_2[i] :
            return 2

def one_pair(p1,p2):
    num_1 = [num_dict[card[0]] for card in p1]
    num_2 = [num_dict[card[0]] for card in p2]

    dic_1 = Counter(num_1)
    dic_2 = Counter(num_2)


    for card in dic_1.copy():
        if dic_1[card] != 2 :
            dic_1.pop(card)

    for card in dic_2.copy():
        if dic_2[card] != 2 :
            dic_2.pop(card)


    dic_1 = sorted(dic_1,key=lambda card: Counter(num_1)[card],reverse = True)  
    dic_2 = sorted(dic_2,key=lambda card: Counter(num_2)[card],reverse = True)  

    #print(dic_1)

    if len(dic_1) == 0 and len(dic_2) == 0:
        return False
    elif len(dic_1) > len(dic_2):
        return 1
    elif len(dic_1) < len(dic_2):
        return 2
    elif len(dic_2) == 0:
        return 1
    elif len(dic_1) == 0:
        return 2
    elif len(dic_1) == 1 and len(dic_2) == 1:
        if dic_1[0] > dic_2[0]:
            return 1
        elif dic_1[0] < dic_2[0]:
            return 2
        else:
            return high_card(p1,p2)
    elif len(dic_1) == 2 and len(dic_2) == 2:
        for i in range(2):
            if dic_1[i] > dic_2[i]:
                return 1
            elif dic_1[i] < dic_2[i]:
                return 2
        return high_card(p1,p2)
    else:
        return "Error one pair"



def three_four(p1,p2,val):
    num_1 = [num_dict[card[0]] for card in p1]
    num_2 = [num_dict[card[0]] for card in p2]

    dic_1 = Counter(num_1)
    dic_2 = Counter(num_2)

    
    for card in dic_1.copy():
        if dic_1[card] != val :
            dic_1.pop(card)

    for card in dic_2.copy():
        if dic_2[card] != val :
            dic_2.pop(card)

    dic_1 = sorted(dic_1,key=lambda card: Counter(num_1)[card],reverse = True)  
    dic_2 = sorted(dic_2,key=lambda card: Counter(num_2)[card],reverse = True)
    #print(dic_1,dic_2)

    if len(dic_1) == 0 and len(dic_2) == 0:
        return False
    elif len(dic_2) == 0:
        return 1
    elif len(dic_1) == 0:
        return 2
    elif len(dic_1) == 1 and len(dic_2) == 1:
        if dic_1[0] > dic_2[0]:
            return 1
        elif dic_1[0] < dic_2[0]:
            return 2
        else:
            return high_card(p1,p2)
    else:
        return "Error three four"



def straight(p1,p2):
    num_1 = [num_dict[card[0]] for card in p1]
    num_2 = [num_dict[card[0]] for card in p2]


    dic_1 = Counter(num_1)
    dic_2 = Counter(num_2)


    for card in dic_1.copy():
        if dic_1[card] != 1 :
            dic_1.pop(card)

    for card in dic_2.copy():
        if dic_2[card] != 1 :
            dic_2.pop(card)

    #print(dic_2.keys())
    dic_1 = sorted(dic_1.keys(),reverse = True)  
    dic_2 = sorted(dic_2.keys(),reverse = True)


    #print(dic_1,dic_2)
    if len(dic_1) != 5 and len(dic_2) != 5:
        return False
    
    elif (len(dic_2) != 5 or dic_2[0] - dic_2[-1]  != 4)  and dic_1[0] - dic_1[-1]  == 4:
        return 1
    elif (len(dic_1) != 5 or dic_1[0] - dic_1[-1]  != 4) and dic_2[0] - dic_2[-1]  == 4:
        return 2
    elif dic_1[-1] - dic_1[0]  == -4 and dic_2[-1] - dic_2[0]  == -4:
        if dic_1[0] > dic_2[0] :
                return 1
        elif dic_1[0] < dic_2[0] :
                return 2
        return False
    else:
        return False

def flush(p1,p2):
    num_1 = [card[1] for card in p1]
    num_2 = [card[1] for card in p2]

    num_1 = len(Counter(num_1).keys())
    num_2 = len(Counter(num_2).keys())

    #print(num_1,num_2)
    if num_1 ==1 and num_2 !=1:
        return 1
    elif num_1 != 1 and num_2 == 1:
        return 2
    else:
        return False
        
def full_house(p1,p2):
    num_1 = [num_dict[card[0]] for card in p1]
    num_2 = [num_dict[card[0]] for card in p2]

    dic_1 = Counter(num_1)
    dic_2 = Counter(num_2)


    
    for card in dic_1.copy():
        if dic_1[card] != 2 and dic_1[card] != 3 :
            dic_1.pop(card)

    for card in dic_2.copy():
        if dic_2[card] != 2 and dic_2[card] != 3 :
            dic_2.pop(card)


    dic_1 = sorted(dic_1,key=lambda card: Counter(num_1)[card],reverse = True)  
    dic_2 = sorted(dic_2,key=lambda card: Counter(num_2)[card],reverse = True)  

    #print(dic_1,dic_2)

    if len(dic_1) == 0 and len(dic_2) == 0:
        return False
    elif len(dic_2) == 0 and len(dic_1) == 2:
        return 1
    elif len(dic_1) == 0 and len(dic_2) == 2:
        return 2
    elif len(dic_1) == 2 and len(dic_2) == 2:
        if dic_1[0] > dic_2[0]:
            return 1
        elif dic_1[0] < dic_2[0]:
            return 2
        if dic_1[1] > dic_2[1]:
            return 1
        elif dic_1[1] < dic_2[1]:
            return 2
        else:
            return False
    else:
        return False
    
def straight_flush(p1,p2):
    if flush(p1,p2):
        return straight(p1,p2)



def winner(p1,p2):
    if straight_flush(p1,p2):
        #print("straight flush")
        return straight_flush(p1,p2)
    elif three_four(p1,p2,4):
        #print("four kind")
        return three_four(p1,p2,4)
    elif full_house(p1,p2):
        #print("full house")
        return full_house(p1,p2)
    elif flush(p1,p2):
        #print("flush")
        return flush(p1,p2)
    elif straight(p1,p2):
        #print("straight")
        return straight(p1,p2)
    elif three_four(p1,p2,3):
        #print("three of a kind")
        return three_four(p1,p2,3)
    elif one_pair(p1,p2):
        #print("one or two pair")
        return one_pair(p1,p2)
    elif high_card(p1,p2):
        #print("High card")
        return high_card(p1,p2)
    else:
        print("SAME")


p1 = "2H 2D 4C 4D 4S"
p2 = "3C 3D 3S 9S 9D"

f = open("poker.txt", "r")

one_win = 0
for p in f:
    p1 = p[:14]
    p2 = p[15:-1]
    #break
    if (winner(p1.split(" "),p2.split(" "))) == 1:
        one_win += 1

print(one_win)
f.close()
