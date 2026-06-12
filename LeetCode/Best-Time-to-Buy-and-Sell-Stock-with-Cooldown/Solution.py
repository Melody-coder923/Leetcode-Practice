1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        n=len(prices)
4        dp=[[0]*2 for _ in range(n)]
5
6        dp[0][0] = 0
7        dp[0][1] = -prices[0]
8        for i in range(1,n):
9            if i==1:
10                #不持有
11                dp[i][0]=max(dp[i-1][0],dp[i-1][1]+prices[i])
12                #持有
13                dp[i][1] = max(dp[i-1][1], -prices[i])
14            #不持有 cool down one day
15            dp[i][0]=max(dp[i-1][0],dp[i-1][1]+prices[i])
16            #持有
17            dp[i][1]=max(dp[i-1][1],dp[i-2][0]-prices[i])
18
19        return dp[n-1][0]