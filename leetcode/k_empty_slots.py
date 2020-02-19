import bisect

class Solution:
    
    def check_status(self, cur_live_bulb):
                
        if(len(self.live_bulbs)>=2):
            idx = self.live_bulbs.index(cur_live_bulb)
            if(idx-1>=0 and (self.live_bulbs[idx]-self.live_bulbs[idx-1]-1)==self.K):
                return True
            elif(idx+1<=len(self.live_bulbs)-1 and (self.live_bulbs[idx+1]-self.live_bulbs[idx]-1)==self.K):
                return True
            
        return False
                
    
    def kEmptySlots(self, bulbs: List[int], K: int) -> int:
        bulb_status = [0 for b in bulbs]
        found = False
        self.live_bulbs = []
        self.K = K
        
        for d in range(1, max(bulbs)+1):
            bulb_status[bulbs[d-1]-1] = 1
            
            bisect.insort(self.live_bulbs, bulbs[d-1])
            
            if(self.check_status(bulbs[d-1])):
                found = True
                break
        
        if(found):
            return d
        return -1
