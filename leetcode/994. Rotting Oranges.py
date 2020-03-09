import queue as queue

class Solution:

    def orangesRotting(self, grid: List[List[int]]) -> int:
        days = 0
        q = queue.Queue()
        fresh_oranges_count = 0
        x, y = len(grid), len(grid[0])
        
        initial_rotten_batch = []
        for i in range(x):
            for j in range(y):
                if(grid[i][j]==2):
                    initial_rotten_batch.append((i,j))
                elif(grid[i][j]):
                    fresh_oranges_count += 1
        q.put(initial_rotten_batch)
        
        while(not q.empty()):
            rotten_batch = q.get()
            days+=1
            next_batch = []
            
            for (i,j) in rotten_batch:
                if(i-1>=0 and grid[i-1][j]==1):
                    next_batch.append((i-1, j))
                    fresh_oranges_count-=1
                    grid[i-1][j] = 2
                if(i+1<=x-1 and grid[i+1][j]==1):
                    next_batch.append((i+1, j))
                    fresh_oranges_count-=1
                    grid[i+1][j] = 2
                if(j-1>=0 and grid[i][j-1]==1):
                    next_batch.append((i, j-1))
                    fresh_oranges_count-=1
                    grid[i][j-1] = 2
                if(j+1<=y-1 and grid[i][j+1]==1):
                    next_batch.append((i, j+1))
                    fresh_oranges_count-=1
                    grid[i][j+1] = 2
            
            if(next_batch!=[]):
                q.put(next_batch)
            
        if(fresh_oranges_count>0):
            return -1
        return days-1    
