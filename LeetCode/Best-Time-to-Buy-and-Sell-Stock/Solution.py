1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        """
4        day hold
5        day not hold
6
7        dp[day][status]
8           
9        """
10        n=len(prices)
11        #build dp
12        dp= [[0]*2 for _ in range(n)]
13        # inti
14        dp[0][1]= -prices[0]
15        for i in range(1,n):
16            dp[i][0]=max(dp[i-1][0],dp[i-1][1]+prices[i])
17            dp[i][1]=max(dp[i-1][1],-prices[i])
18        
19        return dp[n-1][0]
20
21