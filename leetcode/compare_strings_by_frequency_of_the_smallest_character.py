from bisect import bisect

class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        query_counts = []
        word_counts = []
        
        for item in queries:
            query_counts.append(item.count(min(item)))
        
        for item in words:
            word_counts.append(item.count(min(item)))
        
        word_counts.sort()
        
        res = []
        for item in query_counts:
            count = len(word_counts) - bisect(word_counts, item)
            res.append(count)
    
        return res
    
