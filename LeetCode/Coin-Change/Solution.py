1class Solution:
2    def coinChange(self, coins: List[int], amount: int) -> int:
3        n=len(coins)
4        dp= [[float("inf")]* (amount+1) for _ in range(n+1)]
5        
6        for i in range(n+1):
7            dp[i][0]= 0
8        
9        for i in range(1, n+1):
10            for j in range(1,amount+1):
11                #不取：
12                dp[i][j]=dp[i-1][j]
13                #取
14                if j-coins[i-1]>=0 and dp[i][j-coins[i-1]]!=float("inf"):
15                    dp[i][j]=min(dp[i][j-coins[i-1]]+1, dp[i][j])
16        
17        return -1 if dp[n][amount] == float("inf") else dp[n][amount]
18
19