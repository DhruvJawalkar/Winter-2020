class Solution:
def is_number_valid_after_rotation(self, n):
    str_n = str(n)
    str_n = str_n.replace('0','')
    str_n = str_n.replace('1','')
    str_n = str_n.replace('8','')
    
    if(str==''):
        return False
    
    if(('3' in str_n) or ('4' in str_n) or ('7' in str_n)):
        return False
    
    if(len(str_n)):
        return True
    return False
    
    
def rotatedDigits(self, N: int) -> int:
    counter = 0
    
    for n in range(1,N+1):
        if(self.is_number_valid_after_rotation(n)):
            counter+=1
    
    return counter
    
