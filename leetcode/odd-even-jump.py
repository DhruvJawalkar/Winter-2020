class Solution:
def find_nearest(self, idxs, i, is_odd_jump):
    for j in range(i+1, len(idxs)):
        if(idxs[i]<idxs[j]):
            return idxs[j]
    return None

    

def get_jump_idx(self, i, idxs_inc, idxs_dec, is_odd_jump):
    j = None
    
    if(is_odd_jump):
        #find index of i in idxs_inc
        pos = idxs_inc.index(i)
        #find nearest sibling index>=i in subarray idxs_inc[pos+1:]
        j = self.find_nearest(idxs_inc, pos, is_odd_jump)
        if(j is not None):
            return j
    else:
        pos = idxs_dec.index(i)
        #find nearest sibling index>=i in subarray idxs_inc[pos+1:]
        j = self.find_nearest(idxs_dec, pos, is_odd_jump)
        if(j is not None):
            return j
    
    return j

def oddEvenJumps(self, A: List[int]) -> int:
    n_items = len(A)
    odd = []
    even = []
    
    for i in range(n_items):
        odd.append(False)
        even.append(False)
    
    odd[n_items-1] = True
    even[n_items-1] = True
    
    idxs_inc = [i[0] for i in sorted(enumerate(A), key=lambda x:x[1])]
    idxs_dec = [i[0] for i in sorted(enumerate(A), key=lambda x:x[1], reverse=True)]
    
    for idx in range(n_items-2, -1, -1):
        odd_jump_idx = self.get_jump_idx(idx, idxs_inc, idxs_dec, True)
        even_jump_idx = self.get_jump_idx(idx, idxs_inc, idxs_dec, False)
        
        if(odd_jump_idx is not None):
            odd[idx] = even[odd_jump_idx]
        if(even_jump_idx is not None):
            even[idx] = odd[even_jump_idx]
    #print(odd)
    return sum(odd)
    
        
    
