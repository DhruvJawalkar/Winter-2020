from collections import defaultdict

class AutocompleteSystem:

    def reset(self):
        self.query_string = ''
        self.results = []
    
    def update_query_string(self, c):
        self.query_string = self.query_string+c
        
    def __init__(self, sentences: List[str], times: List[int]):
        self.dataset = sentences
        self.hotness = defaultdict(lambda: 0)
        
        for idx, val in enumerate(times):
            self.hotness[sentences[idx]] = val
        
        self.query_string = ''
        self.results = []
      
    def match_by_prefix(self):
        if(len(self.results)):
            matching_arr = self.results
        else:
            matching_arr = self.dataset
        
        results = []
        for sentence in matching_arr:
            try:
                if(sentence.index(self.query_string)==0):
                    results.append(sentence)
            except:
                continue
        self.results = results
        
    def order_by_hotness(self):
        self.results = sorted(self.results, key = lambda x: (-self.hotness[x], x))
    
    def save_query_string(self):
        if(self.hotness[self.query_string]):
            self.hotness[self.query_string]+=1
        else:
            self.hotness[self.query_string]=1
            self.dataset.append(self.query_string)
    
    def input(self, c: str) -> List[str]:
        if(c!='#'):
            self.update_query_string(c)
            self.match_by_prefix()
            self.order_by_hotness()
            return self.results[:3]
        else:
            self.save_query_string()
            self.reset()
            
        


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
