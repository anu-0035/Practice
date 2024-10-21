class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        uniques = set()
        n = len(s)
        def dfs(i):
            if i == n: return 0
            res = 0
            for j in range(i,n):
                substr = s[i:j+1]
                if substr in uniques :
                    continue
                uniques.add(substr)
                res = max(res, 1 + dfs(j+1))
                uniques.remove(substr)
            return res
        return dfs(0)
        
