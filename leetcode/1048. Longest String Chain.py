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
