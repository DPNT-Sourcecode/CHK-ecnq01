

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    import math
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
        
        if a_deals > 3:
            no_a_deals = a_deals%3
            if no_a_deals == 0:
                A_three = a_deals/3 * 130
            else:
                A_three = math.floor(a_deals/3) * 130 + 50* (a_deals%3)
        
        if b_deals > 2:
            no_b_deals = b_deals%3
            if no_b_deals == 0:
                B_two = b_deals/2 * 45
            else:
                B_two = math.floor(a_deals/2) * 45 + 30* (a_deals%2)
            
        rest = [a for a in re if a != 50 and a != 30]
        ret = sum(rest)


    except:
        ret = -1
 
    return ret






