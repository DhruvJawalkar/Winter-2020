from collections import defaultdict

class Solution:
    def dfs_visit(self, node, visited, adjacency_list):
        for neighbour in adjacency_list[node]:
            if(not visited[neighbour]):
                visited[neighbour]=True
                self.dfs_visit(neighbour, visited, adjacency_list)
                
    
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        counter = 0
        visited = defaultdict(lambda:False)
        for node in range(n):
            visited[node] = False
        
        adjacency_list = defaultdict(lambda:set())
        
        for pair in edges:
            adjacency_list[pair[0]].add(pair[1])
            adjacency_list[pair[1]].add(pair[0])
        
        for node in range(n):
            if(not visited[node]):
                counter +=1
                visited[node] = True
                self.dfs_visit(node, visited, adjacency_list)
        
        return counter
        
