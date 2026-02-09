1class Solution:
2    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
3        m,n=len(s1),len(s2)
4        if m+n!=len(s3):
5            return False
6        dp= [[False]*(n+1) for _ in range(m+1)]
7        dp[0][0]=True
8        for i in range(m+1):
9            for j in range(n+1):
10                if i>0 and s1[i-1]==s3[i+j-1]:
11                    dp[i][j]=dp[i][j] or dp[i-1][j]
12                if j>0 and s2[j-1]==s3[i+j-1]:
13                    dp[i][j] = dp[i][j] or dp[i][j-1]
14        return dp[m][n]