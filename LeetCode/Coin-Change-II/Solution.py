1from typing import List
2class Solution:
3    def change(self, amount: int, coins: List[int]) -> int:
4        dp = [0] * (amount + 1)
5        dp[0] = 1
6         # 关键：外层遍历硬币
7        for coin in coins:
8            # 内层遍历金额
9            for i in range(coin, amount + 1):
10                dp[i] += dp[i - coin]
11        return dp[amount]