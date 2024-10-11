class Solution:
    def rearrange(self, arr):
        #Code here
        n = len(arr)
        ans = [-1] * n
        for i in arr:
            if i == -1:
                continue
            ans[i] = i
        return ans
