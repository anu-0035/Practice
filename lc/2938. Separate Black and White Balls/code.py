class Solution:
    def minimumSteps(self, s: str) -> int:
        # l,ans = 0,0
        # for r in range(len(s)):
        #     if s[r] == '0':
        #         ans += (r-l)
        #         l += 1
        # return ans
        ans, swaps = 0, 0
        for c in s:
            if c == '1':
                swaps += 1
            else:
                ans += swaps
        return ans
         
