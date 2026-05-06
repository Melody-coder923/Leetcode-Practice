1class Solution:
2    def uniquePaths(self, m: int, n: int) -> int:
3        dp = [[0] * n for _ in range(m)]
4        for i in range(m):
5            dp[i][0] = 1
6        for j in range(n):
7            dp[0][j] = 1
8        for i in range(1, m):
9            for j in range(1, n):
10                dp[i][j] = dp[i-1][j] + dp[i][j-1]
11        return dp[m-1][n-1]