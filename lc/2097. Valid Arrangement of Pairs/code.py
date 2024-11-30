# class Solution:
#     def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
#         graph = defaultdict(list)
#         in_degree = defaultdict(int)
#         out_degree = defaultdict(int)

#         for start,end in pairs:
#             graph[start].append(end)
#             in_degree[end] += 1
#             out_degree[start] += 1
        
#         start_node = None
#         for node in graph:
#             if out_degree[node] > in_degree[node]:
#                 start_node = node
#                 break
#         if not start_node:
#             start_node = pairs[0][0]
        
#         stack = [start_node]
#         path = []

#         while stack:
#             while graph[stack[-1]]:
#                 next_node = graph[stack[-1]].pop()
#                 stack.append(next_node)
#             path.append(stack.pop())
#         path.reverse()
#         res = [[path[i],path[i+1]] for i in range(len(path)-1)]
#         return res

from collections import defaultdict
from typing import List

class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        inOutDeg = defaultdict(int)

        for start, end in pairs:
            graph[start].append(end)
            inOutDeg[start] += 1
            inOutDeg[end] -= 1

        startNode = pairs[0][0]
        for node in inOutDeg:
            if inOutDeg[node] == 1:
                startNode = node
                break

        path = []

        def dfs(curr):
            while graph[curr]:
                nextNode = graph[curr].pop()
                dfs(nextNode)
                path.append([curr, nextNode])

        dfs(startNode)
        return path[::-1]

        
