class Solution:
def visit_neighbourhood(self, i, j, grid, visited):
    if(j-1>=0 and (not visited[i][j-1]) and int(grid[i][j-1])):
        visited[i][j-1] = True
        self.visit_neighbourhood(i, j-1, grid, visited)
    if(j+1<=len(grid[0])-1 and (not visited[i][j+1]) and int(grid[i][j+1])):
        visited[i][j+1] = True
        self.visit_neighbourhood(i, j+1, grid, visited)
    if(i-1>=0 and (not visited[i-1][j]) and int(grid[i-1][j])):
        visited[i-1][j] = True
        self.visit_neighbourhood(i-1, j, grid, visited)
    if(i+1<=len(grid)-1 and (not visited[i+1][j]) and int(grid[i+1][j])):
        visited[i+1][j] = True
        self.visit_neighbourhood(i+1, j, grid, visited)
        
def numIslands(self, grid: List[List[str]]) -> int:
    counter = 0
    visited = []
    for i in range(len(grid)):
        visited.append([])
        for j in range(len(grid[0])):
            visited[i].append(False)
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if(int(grid[i][j]) and not visited[i][j]):
                counter+=1
                visited[i][j] = True
                self.visit_neighbourhood(i, j, grid, visited)
    
    return counter
