1class Solution:
2    def coinChange(self, coins: List[int], amount: int) -> int:
3        m=len(coins)
4        # 用前 i 个硬币，凑出金额 j 的“最少硬币数”
5        dp= [[float("inf")]* (amount+1) for _ in range(m+1)] 
6
7        for i in range(m+1):
8            dp[i][0]=0
9
10        for i in range(1,m+1):
11            for j in range(1,amount+1):
12                dp[i][j]=dp[i-1][j] #不用
13                if j>=coins[i-1] and dp[i][j-coins[i-1]]!=float("inf"): #用
14                    dp[i][j]=min(dp[i][j],dp[i][j-coins[i-1]]+1) 
15        return dp[m][amount] if dp[m][amount]!=float("inf") else -1
16
17
18    """
19            amounts
20              0  1. 2  3  4  5 6 7 8 9 10 11
21    coins 0   0. e  e. e  e. e e e e e e   e
22          1   0  
23          2   0
24          5   0
25
26    """
27