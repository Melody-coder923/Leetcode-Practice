1class Solution:
2    def minDistance(self, word1: str, word2: str) -> int:
3        m,n=len(word1),len(word2)
4        if m==0:
5            return n
6        if n==0:
7            return m
8        dp= [ [0]*(n+1) for _ in range(m+1) ]
9        for i in range(m+1):
10            dp[i][0]=i
11        for j in range(n+1):
12            dp[0][j]=j
13        for i in range(1,m+1):
14            for j in range(1,n+1):
15                if word1[i-1]==word2[j-1]:
16                    dp[i][j]=dp[i-1][j-1]
17                else:
18                    dp[i][j]= min( 
19                        dp[i-1][j-1],
20                        dp[i-1][j],
21                        dp[i][j-1]
22                    )+1
23        return dp[-1][-1] 