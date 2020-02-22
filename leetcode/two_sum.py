class Solution:
def twoSum(self, nums: List[int], target: int) -> List[int]:
    
    for i in range(len(nums)):
        try:
            filler_elem_idx = nums.index(target-nums[i])
        except:
            filler_elem_idx = -1
            
        if(filler_elem_idx!=-1 and filler_elem_idx!=i):
            return [i, filler_elem_idx]
    return []
        
