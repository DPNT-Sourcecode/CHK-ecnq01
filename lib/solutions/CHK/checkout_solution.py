

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    try:
        values = [a for a in skus]


        dic = {'A':50,'B':30,'C':20,'D':15}
        re = []
        deals = []
        for key in values:
            re.append(dic[key])
            deals.append(key)
        
        a_deals = deals.count('A')
        b_deals = deals.count('B')
        
        if a_deals >= 3 and a_deals < 6:
            A_three = 130
            A_three = A_three + (a_deals-3)*50
        elif a_deals >= 6:
            A_three = 260
            A_three = A_three + (a_deals-6)*50
        elif a_deals < 3:
            A_three = 0
        
        if b_deals >= 2 and b_deals < 4:
            B_two = 45
            B_two = B_two + (b_deals-2)*30
        elif b_deals >= 4:
            B_two = 90
            B_two = B_two + (b_deals-4)*30
        elif b_deals < 2:
            B_two = 0
            
        if B_two == 0  and A_three == 0:
            ret = sum(re)
        elif B_two == 0 and A_three != 0:
            ret = sum([a for a in re if a != 50])  + A_three
        elif B_two != 0 and A_three == 0:
            ret = sum([a for a in re if a !=30]) + B_two 

    except:
        ret = -1
 
    return ret


