1class Solution:
2    def isMatch(self, s: str, p: str) -> bool:
3        m,n=len(s),len(p)
4        dp= [[False]* (n+1) for _ in range(m+1) ]
5        #初始化
6        dp[0][0]=True
7        for j in range(2,n+1):
8            if p[j-1]=="*":
9                dp[0][j]= dp[0][j-2]
10        for i in range(1,m+1):
11            for j in range(1,n+1):
12                #不是*
13                if p[j-1] != "*":
14                    if p[j-1]=="." or p[j-1]==s[i-1]:
15                        dp[i][j]=dp[i-1][j-1]
16                #是*
17                else:
18                    #出现0次
19                    zeromatch=dp[i][j-2] 
20                    #出现多次
21                    multimatch=(s[i-1]==p[j-2] or p[j-2]==".")
22                    if multimatch:
23                        multimatch=dp[i-1][j]
24                    dp[i][j]=zeromatch or multimatch
25        return dp[m][n]
26