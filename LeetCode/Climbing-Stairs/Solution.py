1class Solution:
2    def climbStairs(self, n: int) -> int:
3        if n <= 1:
4            return 1
5        dp = [0] * (n + 1)
6        dp[0]=1
7        dp[1]=1
8        for i in range(2, n + 1):
9            dp[i] = dp[i - 1] + dp[i - 2]
10        return dp[n]
11       