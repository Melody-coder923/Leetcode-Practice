1class Solution:
2    def isMatch(self, s: str, p: str) -> bool:
3        m,n=len(s),len(p)
4        dp=[[False]*(n+1) for _ in range(m+1)]
5        dp[0][0]=True
6        
7        for j in range(2,n+1):
8            if p[j-1]=="*":
9                dp[0][j]=dp[0][j-2]
10
11        for i in range(1,m+1):
12            for j in range(1,n+1):
13                if p[j-1]!="*":
14                    if p[j-1]==s[i-1] or p[j-1]==".":
15                        dp[i][j]=dp[i-1][j-1]
16                else:
17                    zeromatch=dp[i][j-2]
18                    multimatch= (p[j-2] == "." or s[i-1]==p[j-2])
19                    if multimatch:
20                        multimatch=dp[i-1][j]
21                    dp[i][j]=zeromatch or multimatch
22        return dp[m][n]