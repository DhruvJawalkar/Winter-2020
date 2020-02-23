class Solution:
def reverse(self, x: int) -> int:
    x_str = str(x)
    isNegative = False
    
    if(x_str[0]=='-'):
        isNegative = True
        x_str = x_str[1:]
    x_str = x_str[::-1]
    reversed_int = int(x_str)
    if(isNegative):
        reversed_int = -1*reversed_int
    if(reversed_int< -1*2**31 or reversed_int >2**31 -1):
        return 0
    return reversed_int
