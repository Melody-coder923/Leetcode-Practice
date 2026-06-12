1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        n = len(prices)
4        if n == 1:
5            return 0
6        dp = [[0] * 2 for _ in range(n)]
7
8        dp[0][0] = 0
9        dp[0][1] = -prices[0]
10
11        dp[1][0] = max(dp[0][0], dp[0][1] + prices[1])
12        dp[1][1] = max(dp[0][1], -prices[1])
13
14        for i in range(2, n):
15            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
16            dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])
17
18        return dp[n-1][0]