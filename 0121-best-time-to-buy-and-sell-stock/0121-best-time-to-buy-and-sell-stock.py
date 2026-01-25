class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #dp[i]天数[0]不持有[1]持有
        n=len(prices)
        if n == 0:
            return 0
        dp = [[0]*2 for _ in range(n)]
        for i in range(n):
            if i==0:
                dp[i][0]= 0
                dp[i][1]= -prices[i]
                continue
            dp[i][0]=max(dp[i-1][0],dp[i-1][1]+prices[i])
            dp[i][1]=max(dp[i-1][1],- prices[i])
        return dp[n-1][0]