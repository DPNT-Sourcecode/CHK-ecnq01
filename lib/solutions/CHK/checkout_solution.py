

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
     
            ret = sum(ret)
            
        A_three = 130
        B_two = 45
        ret = A
    except:
        ret = -1
 
    return ret
