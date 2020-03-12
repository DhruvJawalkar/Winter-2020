from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        if(len(s)==0):
            return True
        
        matching = dict()
        matching['('] = ')'
        matching['{'] = '}'
        matching['['] = ']'
        stack = deque()
        
        for lit in s:
            if(lit=='(' or lit=='[' or lit=='{'):
                stack.append(lit)
            elif(lit):
                try:
                    top = stack.pop()
                except:
                    return False
                if(matching[top]==lit):
                    continue
                else:
                    return False
                
        if(len(stack)):
            return False
        return True        
