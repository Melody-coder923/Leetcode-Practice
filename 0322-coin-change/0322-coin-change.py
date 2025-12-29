class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #物品: coins -i (可重复)
        #背包: amount -j 
        m=len(coins)
        dp= [[float("inf")] * (amount+1) for _ in range(m+1)]
        for i in range(m+1):
            dp[i][0]=0
        
        for i in range(1,m+1):
            for j in range(amount+1):
                dp[i][j]=dp[i-1][j]
                if j>=coins[i-1] and dp[i][j-coins[i-1]]!=float("inf"):
                    dp[i][j]=min(dp[i][j],dp[i][j-coins[i-1]]+1)
        return dp[m][amount] if dp[m][amount]!=float("inf") else -1
