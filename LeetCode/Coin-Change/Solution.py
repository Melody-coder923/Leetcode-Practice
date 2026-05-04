1class Solution:
2    def coinChange(self, coins: List[int], amount: int) -> int:
3        """dp[i] 表示凑出金额 i 所需的最少硬币数"""
4        dp = [float('inf')] * (amount + 1)
5        dp[0] = 0
6
7        for coin in coins:
8            for i in range(coin, amount + 1):
9                dp[i] = min(dp[i], dp[i - coin] + 1)
10
11        return dp[amount] if dp[amount] != float('inf') else -1