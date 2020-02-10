from collections import defaultdict

class Solution:
    def dfs_visit(self, n, adj_list, edge_weights, visited, cur_time, res):
        for node in adj_list[n]:
            if(not visited[node]):
                visited[node] = True
                res['time'] = max(res['time'], cur_time+edge_weights[(n, node)])
                self.dfs_visit(node, adj_list, edge_weights, visited, cur_time+edge_weights[(n, node)], res)
        return
        
    def dfs(self, k, adj_list, edge_weights, nodes):
        lvl = 0
        res = {
            'time' : 0
        }
        visited = defaultdict(lambda: False)
        visited[k] = True
        for n in adj_list[k]:
            if(not visited[n]):
                visited[n] = True
                res['time'] = max(res['time'], edge_weights[(k, n)])
                self.dfs_visit(n, adj_list, edge_weights, visited, edge_weights[(k, n)], res)
                
        for n in nodes:
            if(not visited[n]):
                return -1
        return res['time']
        
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        nodes = []
        adj_list = defaultdict(lambda:[])
        edge_weights = defaultdict(lambda : 0)
        
        for sub_arr in times:
            if(sub_arr[0] not in nodes):
                nodes.append(sub_arr[0])
            if(sub_arr[1] not in nodes):
                nodes.append(sub_arr[1])
            if(sub_arr[1] not in adj_list[sub_arr[0]]):
                adj_list[sub_arr[0]].append(sub_arr[1])
            ##if(sub_arr[0] not in adj_list[sub_arr[1]]):
            ##    adj_list[sub_arr[1]].append(sub_arr[0])
            
            edge_weights[(sub_arr[0], sub_arr[1])] = sub_arr[2]
            
        return self.dfs(K, adj_list, edge_weights, nodes)     
