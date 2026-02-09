1class Solution:
2    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
3        # dp i 和 j 前i个s1 和前j个s2 是否可以组成s3
4        m,n=len(s1),len(s2)
5        #Edge Case
6        if m+n!=len(s3):
7            return False
8        # dp initialzation
9        dp= [[False]*(n+1) for _ in range(m+1)]
10        for i in range(m+1):
11            for j in range(n+1):
12                if i==0 and j==0:
13                    dp[i][j]=True
14                else:
15                    if i>0 and s1[i-1]==s3[i+j-1] and dp[i-1][j]:
16                        dp[i][j]= True
17                    if j>0 and s2[j-1]==s3[i+j-1] and dp[i][j-1]:
18                        dp[i][j]= True
19                
20        return dp[m][n]