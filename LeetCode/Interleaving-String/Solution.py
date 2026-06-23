1class Solution:
2    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
3        m,n,t=len(s1),len(s2),len(s3)
4        if m+n!=t:
5            return False
6        
7        dp= [[False]*(n+1) for _ in range(m+1)]
8     
9        for i in range(m+1):
10            for j in range(n+1):
11                if i==0 and j==0:
12                    dp[i][j]=True
13                else:
14                    if i>0 and s1[i-1]==s3[i+j-1] and dp[i-1][j]: 
15                        dp[i][j]=True
16                    if j>0 and s2[j-1]==s3[i+j-1] and dp[i][j-1]:
17                        dp[i][j]=True
18        return dp[m][n]    
19
20"""
21      0 d b b c a  n
22    0 T 
23    a
24    a
25    b
26    c
27    c
28"""