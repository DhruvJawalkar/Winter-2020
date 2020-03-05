#using dynamic programming
from collections import defaultdict

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        l_c = defaultdict(lambda:0)
        l_c[''] = 0
        
        #sort words according to length in ascending order,
        #build dp memory in bottom up fashion
        words.sort(key=lambda w : len(w))
        
        for w in words:
            for i in range(len(w)):
                sub_str = w[:i]+w[i+1:]
                if(sub_str in l_c):
                    l_c[w] = max(l_c[w], 1+l_c[sub_str])
            l_c[w] = max(l_c[w], 1)
        return max(l_c.values())
                    
#conventional recursive sol
class Solution:
def get_longest_chain(self, word, sub_arr):
    if(sub_arr==[]):
        return 0
    longest_chain = 0
    for i in range(len(word)):
        sub_str = word[:i] + word[i+1:]
        if(sub_str in sub_arr):
            idx = sub_arr.index(sub_str)
            longest_chain = max(longest_chain, 1+self.get_longest_chain(sub_str, sub_arr[idx+1:]))
    return longest_chain
    

def longestStrChain(self, words: List[str]) -> int:
    words.sort(key=lambda w: len(w), reverse=True)
    longest_chain = 0
    
    for i in range(len(words)-1):
        longest_chain = max(longest_chain, 1+self.get_longest_chain(words[i], words[i+1:]))
    
    return longest_chain
