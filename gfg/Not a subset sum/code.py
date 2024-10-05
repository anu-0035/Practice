#User function Template for python3

class Solution:
    def findSmallest(self, arr):
        # code here
        ans = 1
        for n in arr:
            if n > ans:
                return ans
            ans += n
        return ans
