1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        n=len(prices)
4        dp=[[0]*2 for _ in range(n)]
5
6        dp[0][0]= 0
7        dp[0][1]= -prices[0]
8        
9
10        for i in range(1,n):
11            dp[i][0]= max(dp[i-1][0],dp[i-1][1]+prices[i])
12            if i==1:
13                dp[i][1]= max(dp[i-1][0]-prices[i],dp[i-1][1])
14            else:
15                dp[i][1]= max(dp[i-2][0]-prices[i],dp[i-1][1])
16        return dp[n-1][0]