class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        prefixXOR = [0] * (n+1)
        for i in range(1,n+1):
            prefixXOR[i] = prefixXOR[i-1] ^ arr[i-1]

        ans = []
        for x,y in queries:
            ans.append(prefixXOR[y+1] ^ prefixXOR[x])
        return ans
        
