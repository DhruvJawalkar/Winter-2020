class ProductOfNumbers:

def __init__(self):
    self.arr = []
    self.precomputed = dict()
    
def add(self, num: int) -> None:
    self.arr.append(num)

def getProduct(self, k: int) -> int:
    if((len(self.arr), k) in self.precomputed):
        return self.precomputed[(len(self.arr), k)]
        
    res_arr = self.arr[-k:]
    res = 1
    for i in res_arr:
        res = res*i
        if(res==0):
            break
    self.precomputed = dict()
    self.precomputed[(len(self.arr), k)] = res
        
    return res
