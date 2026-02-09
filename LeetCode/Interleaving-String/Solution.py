1class Solution:
2    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
3        m,n=len(s1),len(s2)
4        if m + n != len(s3):
5            return False
6        dp = [[False] * (n + 1) for _ in range(m + 1)]
7
8        for i in range(m + 1):
9            for j in range(n + 1):
10                if i==0 and j==0:
11                    dp[i][j]=True
12                else:
13                    if i>0 and s1[i-1]==s3[i+j-1] and dp[i-1][j]:
14                        dp[i][j]=True
15                    if j > 0 and s2[j-1] == s3[i+j-1] and dp[i][j-1]:
16                        dp[i][j]=True
17        return dp[m][n]