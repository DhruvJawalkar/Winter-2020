from collections import defaultdict

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls, cows = 0, 0
        s, g = defaultdict(lambda:0), defaultdict(lambda:0)
        
        for i, digit in enumerate(guess):
            if(secret[i]==guess[i]):
                bulls+=1
            else:
                s[secret[i]]+=1
                g[guess[i]]+=1
       
        for i,val in g.items():
            if(i in s):
                cows+=min(s[i], g[i])
        
        return str(bulls)+'A'+str(cows)+'B'
                
        
        
