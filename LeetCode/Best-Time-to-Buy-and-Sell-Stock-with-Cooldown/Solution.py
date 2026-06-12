1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        n=len(prices)
4        dp = [[0] * 2 for _ in range(n)]
5        for i in range(n):
6            if i-1==-1:
7                dp[i][0]=0
8                dp[i][1]=-prices[i]
9                continue
10            if i-2==-1:
11                dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
12                dp[i][1] = max(dp[i-1][1], -prices[i])
13                continue
14
15            dp[i][0]=max(dp[i-1][0],dp[i-1][1]+prices[i])
16            dp[i][1]=max(dp[i-1][1],dp[i-2][0]-prices[i])
17        return dp[n-1][0]