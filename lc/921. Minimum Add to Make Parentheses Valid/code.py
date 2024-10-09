class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        ans = 0
        open_count = 0
        for c in s:
            if c == "(":
                open_count += 1
            else:
                open_count -= 1
                if open_count < 0:
                    open_count = 0
                    ans += 1

        return open_count + ans

        
