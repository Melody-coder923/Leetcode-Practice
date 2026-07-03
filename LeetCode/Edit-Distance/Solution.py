1class Solution:
2    def minDistance(self, word1: str, word2: str) -> int:
3        m,n=len(word1),len(word2)
4        dp=[[0]*(n+1) for _ in range(m+1)]
5        for i in range(m+1):
6            dp[i][0]=i
7        for j in range(n+1):
8            dp[0][j]=j
9        
10        for i in range(1,m+1):
11            for j in range(1,n+1):
12                if word1[i-1]==word2[j-1]:
13                    dp[i][j]=dp[i-1][j-1]
14                else:
15                    dp[i][j]=min(
16                    #insert
17                    dp[i][j-1],
18                    #delete
19                    dp[i-1][j-1],
20                    #replace
21                    dp[i-1][j]
22                    )+1
23        return dp[m][n]
24"""
25插入看左边，删除看上面，替换看左上角
26       0 r o s
27    0  0 1 2 3
28    h. 1 1 2 3
29    o. 2 2 1 2
30    r. 3 2 2 2
31    s  4 
32    e. 5
33"""