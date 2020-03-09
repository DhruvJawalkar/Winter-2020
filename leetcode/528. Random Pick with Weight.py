import random
import bisect

class Solution:

    def __init__(self, w: List[int]):
        self.arr = [w[0]]
        
        for i in range(1, len(w)):
            self.arr.append(w[i]+self.arr[i-1])
        
        self.ceil = self.arr[-1]
        
        
    def pickIndex(self) -> int:
        choice = random.randint(0, self.ceil-1)
        return bisect.bisect_right(self.arr, choice)


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

#Sol 2 with insert position in sorted array
############################################################################
import random

class Solution:
    def __init__(self, w: List[int]):
        self.arr = [w[0]]
        
        for i in range(1, len(w)):
            self.arr.append(w[i]+self.arr[i-1])
        
        self.ceil = self.arr[-1]
    
    def get_insert_position(self, val):
        lo = 0
        hi = len(self.arr)-1
        
        while(lo!=hi):
            mid = (lo+hi)//2
            
            if(val>=self.arr[mid]):
                lo = mid+1
            else:
                hi = mid
        
        return lo
        
        
    def pickIndex(self) -> int:
        choice = random.randint(0, self.ceil-1)
        idx = self.get_insert_position(choice)
        return idx


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
