

# noinspection PyUnusedLocal
# skus = unicode string
import re
def checkout(skus):
    try:
        values = re.findall(r'\b\w+\b',skus)
        A = 50
        B = 30
        C = 20
        D = 15
        A_three = 130
        B_two = 45
        ret = A
    except:
        ret = -1
 
    return ret



