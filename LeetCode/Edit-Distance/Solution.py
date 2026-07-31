1class Solution:
2    def minDistance(self, word1: str, word2: str) -> int:
3        m,n=len(word1),len(word2)
4        dp= [[0]*(n+1) for _ in range(m+1)]
5        for i in range(m+1):
6            dp[i][0]=i
7        for j in range(n+1):
8            dp[0][j]=j
9        for i in range(1,m+1):
10            for j in range(1,n+1):
11                if word1[i-1]==word2[j-1]:
12                    dp[i][j]= dp[i-1][j-1]
13                else:
14                    dp[i][j]=min(
15                    #insert
16                    dp[i-1][j],
17                    #delete
18                    dp[i][j-1],
19                    #replace
20                    dp[i-1][j-1]
21                    )+1
22
23        return dp[m][n]
24
25
26"""
27  0  r o s
280 0  1 2 3
29h 1. 
30o 2
31r 3
32s 4
33e 5
34"""