#User function Template for python3
from collections import defaultdict
class Solution:
    def isCircle(self, arr):
        # code here
        in_degree = defaultdict(int)
        out_degree = defaultdict(int)
        graph = defaultdict(list)
        
        for s in arr:
            graph[s[0]].append(s[-1])
            out_degree[s[-1]] += 1
            in_degree[s[0]] += 1
        
        for node in set(in_degree.keys()).union(set(out_degree.keys())):
            if in_degree[node] != out_degree[node]:
                return 0
        
        visited = set() 
        def dfs(node):
            visited.add(node)
            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei)
        dfs(arr[0][0])
        
        for node in set(in_degree.keys()).union(set(out_degree.keys())):
            if node not in visited :
                return 0
        
        return 1
