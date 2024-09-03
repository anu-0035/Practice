#User function Template for python3
class Solution:
	def minOperations(self, str1, str2):
		# code here
		n,m = len(str1),len(str2)
		dp = [[0] * (m+1) for _ in range(n+1)]
		for i in range(1,n+1):
		    for j in range(1,m+1):
		        if str1[i-1] == str2[j-1]:
		            dp[i][j] = dp[i-1][j-1] + 1
		        else:
		            dp[i][j] = max(dp[i-1][j],dp[i][j-1])
		lcs_length = dp[n][m]
		insertion  = n - lcs_length
		deletion = m - lcs_length
		return insertion + deletion 
