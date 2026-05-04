1class Solution:
2    def coinChange(self, coins: List[int], amount: int) -> int:
3        #物品: coins -i (可重复)
4        #背包: amount -j 
5        m=len(coins)
6        dp= [[float("inf")] * (amount+1) for _ in range(m+1)]
7        for i in range(m+1):
8            dp[i][0]=0
9        
10        for i in range(1,m+1):
11            for j in range(amount+1):
12                dp[i][j]=dp[i-1][j]
13                if j>=coins[i-1] and dp[i][j-coins[i-1]]!=float("inf"):
14                    dp[i][j]=min(dp[i][j],dp[i][j-coins[i-1]]+1)
15        return dp[m][amount] if dp[m][amount]!=float("inf") else -1
16