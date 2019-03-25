

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    import math
    try:
        values = [a for a in skus]


        dic = {'A':50,'B':30,'C':20,'D':15,'E':40,'F':10}
        re = []
        deals = []
        for key in values:
            re.append(dic[key])
            deals.append(key)
        
        a_deals = deals.count('A')
        b_deals = deals.count('B')
        e_deals = deals.count('E')
        f_deals = deals.count('F')


#        no_a_deals = a_deals%3
        no_a_deals_fiver = a_deals%5
        
        no_e_deals = math.floor(e_deals/2)

        A_three = 0
        
        if no_a_deals_fiver == 0:
            A_three = a_deals/5 * 200
#        elif no_a_deals == 0:
#            A_three = a_deals/3 * 130
        else:
            A_three = math.floor(a_deals/5)*200 +  math.floor((a_deals - math.floor(a_deals/5)*5)/3) * 130 + math.floor(a_deals - math.floor(a_deals/5)*5 - math.floor((a_deals - math.floor(a_deals/5)*5)/3)*3)*50
        
        
        no_b_deals = (b_deals-no_e_deals)%2
        b_deals = max(b_deals - no_e_deals,0)
        if no_b_deals == 0:
            B_two = b_deals/2 * 45
        else:
            B_two = math.floor(b_deals/2) * 45 + 30* (b_deals%2)
            
            
        no_f_deals = f_deals%3    
        if no_f_deals == 0:
            
        rest = [a for a in re if a != 50 and a != 30]
        ret = int(sum(rest) + B_two + A_three)


    except:
        ret = -1
 
    return ret

