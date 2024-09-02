class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n:
            return []
        a = []
        s,e = 0,n
        for i in range(m):
            a.append(original[s:e])        
            s,e = e,e+n
        return a
