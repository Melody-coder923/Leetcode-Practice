1class Solution:
2    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
3        # dp[i][j] = 从 (i,j) 出发，到终点能活下去，所需的最少血量
4        m,n=len(dungeon),len(dungeon[0])
5        dp= [[0]*n for _ in range(m)]
6        dp[m-1][n-1] = max(1, 1 - dungeon[m-1][n-1])
7        # 最后一列
8        for i in range(m-2, -1, -1):
9            dp[i][n-1] = max(1, dp[i+1][n-1] - dungeon[i][n-1])
10        # 最后一行
11        for j in range(n-2, -1, -1):
12            dp[m-1][j] = max(1, dp[m-1][j+1] - dungeon[m-1][j])
13        
14        # 其他位置
15        for i in range(m-2, -1, -1):
16            for j in range(n-2, -1, -1):
17                need = min(dp[i+1][j], dp[i][j+1])
18                dp[i][j] = max(1, need - dungeon[i][j])
19        return dp[0][0]