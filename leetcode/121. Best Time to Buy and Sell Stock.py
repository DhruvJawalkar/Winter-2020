class Solution:
def maxProfit(self, prices: List[int]) -> int:
    if(prices==[]):
        return 0
    
    max_profit = 0
    least_price = prices[0]
    
    for i in range(1, len(prices)):
        if(prices[i]>least_price):
            max_profit = max(prices[i] - least_price, max_profit)
        else:
            least_price = prices[i]
            
    return max_profit     
