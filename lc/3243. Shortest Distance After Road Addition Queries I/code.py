class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        adj = [[i+1] for i in range(n)]
        
        def shortest_path():
            q = deque()
            visit = set()
            visit.add((0,0))
            q.append((0,0))
            while q:
                cur,l = q.popleft()
                if cur == n-1:
                    return l
                for nei in adj[cur]:
                    if nei not in visit:
                        q.append((nei,l+1))
                        visit.add(nei)

        res = []
        for src,des in queries:
            adj[src].append(des)
            res.append(shortest_path())
        return res
        
