class Solution:
def maxSubArray(self, nums: List[int]) -> int:
    if(nums==[]):
        return 0
        
    dp = [0]*len(nums)
    dp[0] = nums[0]
    max_sum = dp[0]
    start_idx, end_idx = 0, 0
    
    for i in range(1, len(nums)):
        if(nums[i]+dp[i-1]>=nums[i]):
            dp[i] = dp[i-1] + nums[i]
        else:
            #start over
            start_idx = i
            dp[i] = nums[i]
        
        if(dp[i]>=max_sum):
            max_sum = dp[i]
            end_idx = i
    
    res_arr = nums[start_idx:end_idx+1]
    return max_sum
    
    
