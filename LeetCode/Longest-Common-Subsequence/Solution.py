1class Solution:
2    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
3        m,n=len(text1),len(text2)
4        dp= [[0]* (n+1) for _ in range(m+1)]
5        
6        for i in range(1,m+1):
7            for j in range(1,n+1):
8                if text1[i-1]==text2[j-1]:
9                    dp[i][j]=dp[i-1][j-1]+1
10                else:
11                    dp[i][j]=max(dp[i][j-1],dp[i-1][j])
12        return dp[m][n]
13"""
14idx 0 1 2
15  0 a c e
160 0 0 0 0
17a 0 1 1 1
18b 0 1 1 1
19c 0 1 2 2
20d 0 1 2 2
21e 0 1 2 3
22"""