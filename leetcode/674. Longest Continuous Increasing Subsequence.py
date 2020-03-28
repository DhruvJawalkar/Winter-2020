class Solution:
def findLengthOfLCIS(self, nums: List[int]) -> int:
    if(nums==[]):
        return 0
    
    max_len = 1
    cur_count = 1
    for i in range(1, len(nums)):
        if(nums[i]>nums[i-1]):
            cur_count += 1
        else:
            max_len = max(max_len, cur_count)
            cur_count = 1
    
    max_len = max(max_len, cur_count)
    return max_len
