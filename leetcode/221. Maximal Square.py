class Solution:
def maximalSquare(self, matrix: List[List[str]]) -> int:
    memory = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]
    max_square = 0
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if(i==0 or j==0 or int(matrix[i][j])==0):
                memory[i][j] = int(matrix[i][j])
            else:
                memory[i][j] = min(memory[i-1][j], memory[i][j-1], memory[i-1][j-1])+1
            
            if(memory[i][j]>max_square):
                max_square = memory[i][j]
    
    return max_square**2
                
##############################################################################

class Solution:
def maximalSquare(self, matrix: List[List[str]]) -> int:
    if(matrix==[]):
        return 0
    
    memory = [0 for j in range(len(matrix[0]))]
    max_square = 0
    prev = 0
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            temp = memory[j]
            
            if(i==0 or j==0 or int(matrix[i][j])==0):
                memory[j] = int(matrix[i][j])
            else:
                memory[j] = min(memory[j-1], memory[j], prev)+1
            
            prev = temp
            max_square = max(memory[j], max_square)
    
    return max_square**2
                
