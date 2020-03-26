class Solution:
def compare_strings(self, str1, str2, dictionary):
    if(len(str2)==0):
        return False
    
    least_length = min(len(str1), len(str2))
    
    for i in range(least_length):
        if(dictionary[str1[i]] < dictionary[str2[i]]):
            return True
        elif(dictionary[str1[i]] > dictionary[str2[i]]):
            return False
    
    return least_length==len(str1)

def isAlienSorted(self, words: List[str], order: str) -> bool:
    if(len(words)<2):
        return True
    
    dictionary = dict()
    
    for i in range(len(order)):
        dictionary[order[i]] = i+1
    
    for i in range(1, len(words)):
        comp_res = self.compare_strings(words[i-1], words[i], dictionary)
        if(comp_res==False):
            return False
    
    return True
