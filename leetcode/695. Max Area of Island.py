class Solution:
def visit_neighbourhood(self, i, j, grid, visited, cur_traversal):
    if(j-1>=0 and (not visited[i][j-1]) and grid[i][j-1]):
        visited[i][j-1] = True
        cur_traversal['depth'] += 1
        self.visit_neighbourhood(i, j-1, grid, visited, cur_traversal)
    if(j+1<=len(grid[0])-1 and (not visited[i][j+1]) and grid[i][j+1]):
        visited[i][j+1] = True
        cur_traversal['depth'] += 1
        self.visit_neighbourhood(i, j+1, grid, visited, cur_traversal)
    if(i-1>=0 and (not visited[i-1][j]) and grid[i-1][j]):
        visited[i-1][j] = True
        cur_traversal['depth'] += 1
        self.visit_neighbourhood(i-1, j, grid, visited, cur_traversal)
    if(i+1<=len(grid)-1 and (not visited[i+1][j]) and grid[i+1][j]):
        visited[i+1][j] = True
        cur_traversal['depth'] += 1
        self.visit_neighbourhood(i+1, j, grid, visited, cur_traversal)

def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    maxArea = 0
    visited = []
    for i in range(len(grid)):
        visited.append([])
        for j in range(len(grid[0])):
            visited[i].append(False)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if(grid[i][j] and not visited[i][j]):
                cur_traversal = dict()
                cur_traversal['depth'] = 1
                visited[i][j] = True
                self.visit_neighbourhood(i, j, grid, visited, cur_traversal)
                if(cur_traversal['depth']>maxArea):
                    maxArea = cur_traversal['depth']
    return maxArea

    
