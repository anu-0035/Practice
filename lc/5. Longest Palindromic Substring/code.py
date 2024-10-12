class Solution(object):
    def longestPalindrome(self, s):
        n=len(s)
        dp=[[False]*(n) for i in range(n)]
        x,m=0,1
        for i in range(n):
            dp[i][i]=True
        for i in range(n-1):
            if(s[i]==s[i+1]):
                dp[i][i+1]=True
                x=i
                m=2
        for i in range(3,n+1):
            for j in range(n-i+1):
                k=j+i-1
                if(s[j]==s[k] and dp[j+1][k-1]):
                    dp[j][k]=True
                    x=j
                    m=i
        return s[x:x+m]
