1class Solution:
2    def isMatch(self, s: str, p: str) -> bool:
3        #Step1:创建dp列表
4        n,m=len(s),len(p)
5        dp=[[False]*(m+1) for _ in range(n+1)]
6
7        #Step2:初始化包括两部分: dp[0][0] ; 以及特殊情况:dp[0][j]情况 如果 p[j-1] 是 '*'，可以跳过前两个字符
8        dp[0][0]=True
9        for j in range(2,m+1):
10            if p[j-1]=="*":
11                dp[0][j]=dp[0][j-2]  
12    
13        #Step3: dp填充
14        for i in range(1,n+1):
15            for j in range(1,m+1):
16        # 情况1: 当前模式不是 '*' (普通字符或者 '.')
17                if p[j-1] != "*":
18                    if s[i-1] == p[j-1] or p[j-1] == '.':
19                        dp[i][j] = dp[i-1][j-1]
20                    
21        # 情况2: 当前模式是 '*' 
22                else: 
23                    # 星号情况1: 代表0个
24                    zeromatch= dp[i][j-2]                
25                    # 星号情况2: 代表1个或多个
26                    multmatch=(s[i-1]==p[j-2] or p[j-2]==".")
27                    if multmatch:
28                        multmatch=dp[i-1][j]
29
30                    dp[i][j] = zeromatch or multmatch
31        return dp[n][m]
32                       
33        