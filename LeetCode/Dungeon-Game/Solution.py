1class Solution:
2    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
3        m,n=len(dungeon),len(dungeon[0])
4        dp= [[0]*n for _ in range(m)]
5        dp[m-1][n-1] = max(1, 1 - dungeon[m-1][n-1])
6        # 最后一列
7        for i in range(m-2, -1, -1):
8            dp[i][n-1] = max(1, dp[i+1][n-1] - dungeon[i][n-1])
9        # 最后一行
10        for j in range(n-2, -1, -1):
11            dp[m-1][j] = max(1, dp[m-1][j+1] - dungeon[m-1][j])
12        
13        # 其他位置
14        for i in range(m-2, -1, -1):
15            for j in range(n-2, -1, -1):
16                need = min(dp[i+1][j], dp[i][j+1])
17                dp[i][j] = max(1, need - dungeon[i][j])
18        return dp[0][0]