1from typing import List
2class Solution:
3    def change(self, amount: int, coins: List[int]) -> int:
4        m=len(coins)
5        dp= [ [0]* (amount+1) for _ in range(m+1) ]
6        for i in range(m+1):
7            dp[i][0]=1
8        for j in range(1,amount+1):
9            dp[0][j]=0
10        for i in range(1,m+1):
11            for j in range(amount+1):
12                dp[i][j]=dp[i-1][j]
13                if j>=coins[i-1]:
14                    dp[i][j]=dp[i-1][j]+dp[i][j-coins[i-1]]
15        return dp[m][amount]
16