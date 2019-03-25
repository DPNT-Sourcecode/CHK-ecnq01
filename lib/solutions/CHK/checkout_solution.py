

# noinspection PyUnusedLocal
# skus = unicode string
import re
def checkout(skus):
    try:
        values = re.findall(r'\b\w+\b',skus)
        dic = {'A':50,'B':30,'C':20,'D':15}
        ret = []
        deals = []
        for key in values:
            print(key)
            ret.append(dic[key])
            deals.append(key)
        
        a_deals = deals.count('A')
        b_deals = deals.count('B')
        
        if a_deals >= 3:
            A_three = 130
            A_three = A_three + (a_deals-3)*50
        elif a_deals < 3:
            A_three = 0
        
        if b_deals >= 2:
            B_two = 45
            B_two = B_two + (b_deals-2)*30
        elif b_deals < 2:
            B_two = 0
            

        ret = A
    except:
        ret = -1
 
    return ret

