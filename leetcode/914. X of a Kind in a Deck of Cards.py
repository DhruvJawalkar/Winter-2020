from math import gcd
from functools import reduce
from collections import Counter

#check to see if gcd of counts is something more than 1
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        counter = Counter(deck)
        card_counts = counter.values()
        final_gcd = reduce(gcd, card_counts)
        
        if(final_gcd>1):
            return True
        return False
                
            
        
