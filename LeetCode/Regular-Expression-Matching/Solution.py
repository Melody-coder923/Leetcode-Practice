1class Solution:
2    def isMatch(self, s: str, p: str) -> bool:
3        m,n=len(s),len(p)
4        dp= [[False]*(n+1) for _ in range(m+1)]
5        dp[0][0]=True
6        for j in range(2,n+1):
7            if p[j-1]=="*":
8                dp[0][j]=dp[0][j-2]
9
10        for i in range(1,m+1):
11            for j in range(1,n+1):
12                if s[i-1]==p[j-1] or p[j-1]==".":
13                    dp[i][j]=dp[i-1][j-1]
14                
15                if p[j-1]=="*":
16                    zeromatch=dp[i][j-2]
17                    multimatch=(s[i-1]==p[j-2] or p[j-2]==".")
18                    if multimatch:
19                        multimatch=dp[i-1][j]
20                    dp[i][j]=zeromatch or multimatch
21        return dp[m][n]