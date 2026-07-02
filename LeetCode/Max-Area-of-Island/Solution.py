1class Solution:
2    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
3        m = len(grid)
4        n = len(grid[0])
5        maxarea = 0
6
7        def dfs(x, y):
8            if x < 0 or y < 0 or x >= m or y >= n or grid[x][y] != 1:
9                return 0
10            grid[x][y] = 0
11            return 1 + dfs(x + 1, y) + dfs(x - 1, y) + dfs(x, y + 1) + dfs(x, y - 1)
12
13        for i in range(m):
14            for j in range(n):
15                if grid[i][j] == 1:
16                    area = dfs(i, j)  # ✅ 获取当前岛屿面积
17                    maxarea = max(maxarea, area)
18
19        return maxarea