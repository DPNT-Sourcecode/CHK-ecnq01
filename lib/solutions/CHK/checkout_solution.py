

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    import math
    try:
        values = [a for a in skus]

        '''
        
#        | H    | 10    | 5H for 45, 10H for 80  |                     |
#        | K    | 80    | 2K for 150             |                       |
        | N    | 40    | 3N get one M free      |
#        | P    | 50    | 5P for 200             |
#        | Q    | 30    | 3Q for 80              |
        | R    | 50    | 3R get one Q free      |                    |
        | U    | 40    | 3U get one U free      |
        | V    | 50    | 2V for 90, 3V for 130  |                      
        '''

        dic = {'A':50,
               'B':30,
               'C':20,'D':15,'E':40,
               'F':10,
               'G':20,'H':10,'I':35,'J':60,'K':80,'L':90,'M':15,'N':40,
               'O':10,'P':50,'Q':30,'R':50,'S':30,'T':20,'U':40,'V':50,
               'W':20,'X':90,'Y':10,'Z':50}

        deals = []
        for key in values:
            try:
                deals.append(key)
            except:
                continue
            
        a_deals = deals.count('A')
        b_deals = deals.count('B')
        e_deals = deals.count('E')
        f_deals = deals.count('F')
        h_deals = deals.count('H')
        k_deals = deals.count('K')
        n_deals = deals.count('N')
        p_deals = deals.count('P')
        q_deals = deals.count('Q')
        r_deals = deals.count('R')
        u_deals = deals.count('U')
        v_deals = deals.count('V')

        dic = {#'A':50,
               #'B':30,
               'C':20,'D':15,'E':40,
               #'F':10,
               'G':20,
               #'H':10,
               'I':35,'J':60,
               #'K':80,
               'L':90,'M':15,'N':40,
               'O':10,
               #'P':50,
               #'Q':30,
               'R':50,'S':30,'T':20,'U':40,'V':50,
               'W':20,'X':90,'Y':10,'Z':50}
        
        re = []
        for key in values:
            try:
                re.append(dic[key])
            except:
                continue
#        no_a_deals = a_deals%3
        no_a_deals_fiver = a_deals%5
        
        '''H'''
        H_five = 0
        h_deals_fiver = h_deals%10
        if h_deals_fiver == 0:
            H_five = h_deals/10 * 80

        
#        elif no_a_deals == 0:
#            A_three = a_deals/3 * 130
        else:
            
            H_five = math.floor(h_deals/10)*80 +  math.floor((h_deals - math.floor(h_deals/10)*10)/5) * 45 + math.floor(h_deals - math.floor(h_deals/10)*10 - math.floor((h_deals - math.floor(h_deals/10)*10)/5)*5)*10

        '''A'''
        A_three = 0
        
        if no_a_deals_fiver == 0:
            A_three = a_deals/5 * 200
#        elif no_a_deals == 0:
#            A_three = a_deals/3 * 130
        else:
            A_three = math.floor(a_deals/5)*200 +  math.floor((a_deals - math.floor(a_deals/5)*5)/3) * 130 + math.floor(a_deals - math.floor(a_deals/5)*5 - math.floor((a_deals - math.floor(a_deals/5)*5)/3)*3)*50
        

        '''K'''
        K_two = 0
        no_k_deals = k_deals%2
        if no_k_deals == 0:
            K_two = k_deals/2 * 150
        else:
            K_two = math.floor(k_deals/2) * 150 + 80* (k_deals%2)

        '''P'''
        P_five = 0
        no_p_deals = p_deals%5
        if no_p_deals == 0:
            P_five = p_deals/5 * 200
        else:
            P_five = math.floor(p_deals/5) * 200 + 50* (p_deals%5)
            
        '''Q'''
        Q_three = 0
        no_q_deals = q_deals%3
        if no_q_deals == 0:
            Q_three = q_deals/3 * 80
        else:
            Q_three = math.floor(q_deals/3) * 80 + 30* (q_deals%3)


            
            
        no_e_deals = math.floor(e_deals/2)
      
        no_b_deals = (b_deals-no_e_deals)%2
        b_deals = max(b_deals - no_e_deals,0)
        if no_b_deals == 0:
            B_two = b_deals/2 * 45
        else:
            B_two = math.floor(b_deals/2) * 45 + 30* (b_deals%2)
            
        F_three = 0
        no_f_deals = f_deals%3    
        if no_f_deals == 0 and f_deals > 0:
            F_three = (f_deals - f_deals/3)*10
        else:
            F_three = math.floor(f_deals/3) *2 * 10 + (f_deals%3)*10
            
            
#        rest = [a for a in re if a != 50 and a != 30 and a != 10]
        ret = int(sum(re) + B_two + A_three + F_three +
                  H_five + K_two + P_five + Q_three)


    except:
        ret = -1
 
    return ret



