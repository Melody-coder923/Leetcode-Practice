1class Solution:
2    def minDistance(self, word1: str, word2: str) -> int:
3        m,n=len(word1),len(word2)
4        dp = [[0] * (n + 1) for _ in range(m + 1)]
5        for j in range(n+1):
6            dp[0][j]= j
7        for i in range(m+1):
8            dp[i][0]=i
9
10        for i in range(1,m+1):
11            for j in range(1,n+1):
12                if word1[i-1]==word2[j-1]:
13                    dp[i][j]=dp[i-1][j-1]
14                else:
15                    dp[i][j]=min(
16                        #删除
17                        dp[i-1][j],
18                        #插入
19                        dp[i][j-1],
20                        #替换
21                        dp[i-1][j-1]
22                    )+1
23        return dp[m][n]