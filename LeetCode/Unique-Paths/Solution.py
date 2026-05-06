1class Solution:
2    def uniquePaths(self, m: int, n: int) -> int:
3        dp=[[0]*n for _ in range(m)] 
4        for j in range(n):
5            dp[0][j]=1
6        for i in range(m):
7            dp[i][0]=1
8        
9        for i in range(1,m):
10            for j in range(1,n):
11                dp[i][j]=dp[i-1][j]+dp[i][j-1]
12        
13        return dp[m-1][n-1]       
14    