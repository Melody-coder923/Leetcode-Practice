1class Solution:
2    #dp[i][j] = 把 word1[:i] 变成 word2[:j] 的最小操作数
3    def minDistance(self, word1: str, word2: str) -> int:
4        m,n=len(word1),len(word2)
5        if m==0:
6            return n
7        if n==0:
8            return m
9        dp= [ [0]*(n+1) for _ in range(m+1) ]
10        #base case
11        for i in range(m+1):
12            dp[i][0]=i
13        for j in range(n+1):
14            dp[0][j]=j
15        
16        for i in range(1,m+1):
17            for j in range(1,n+1):
18                if word1[i-1]==word2[j-1]:
19                    dp[i][j]=dp[i-1][j-1]
20                else:
21                    dp[i][j]=min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
22        return dp[m][n]
23                