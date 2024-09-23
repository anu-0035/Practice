class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        word_list = set(dictionary)
        n = len(s)
        dp = [0] * (n+1)
        dp[0] = 0
        for i in range(1,n+1):
            dp[i] = dp[i-1] +1
            for j in range(i):
                if s[j:i] in word_list:
                    dp[i] = min(dp[i],dp[j])        
        return dp[n]
