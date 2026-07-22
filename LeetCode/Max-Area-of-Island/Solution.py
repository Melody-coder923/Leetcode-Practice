1class Solution:
2    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
3        m,n=len(grid),len(grid[0])
4        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
5        def dfs(x,y):
6            if x < 0 or y < 0 or x >= m or y >= n or grid[x][y] == 0:
7                return 0
8            area=1
9            grid[x][y]=0
10            for dx,dy in directions:
11                nx,ny=x+dx,y+dy
12                area+=dfs(nx,ny)
13            return area
14        res=0    
15        for i in range(m):
16            for j in range(n):
17                if grid[i][j]==1:
18                    res=max(dfs(i,j),res)
19        return res