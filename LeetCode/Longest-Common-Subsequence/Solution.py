1class Solution:
2    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
3        m,n=len(text1),len(text2)
4        dp=[[0]* (n+1) for _ in range(m+1)]
5        for i in range(m+1):
6            dp[i][0]=0
7        for j in range(n+1):
8            dp[0][j]=0
9        for i in range(1,m+1):
10            for j in range(1,n+1):
11                if text1[i-1]==text2[j-1]:
12                    dp[i][j]=dp[i-1][j-1]+1
13                else:
14                    dp[i][j]= max(dp[i-1][j],dp[i][j-1])
15        return dp[m][n]