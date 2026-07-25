1class Solution:
2    def largestIsland(self, grid: List[List[int]]) -> int:
3        n=len(grid)
4        island={}
5        directions=[(1,0),(-1,0),(0,1),(0,-1)]
6        #step1: 分别求面积 mark island id
7        def dfs(x,y,island_id):
8            if x<0 or y<0 or x>=n or y>=n or grid[x][y]!=1:
9                return 0
10            grid[x][y]=island_id
11            area=1
12            for dx,dy in directions:
13                nx,ny=x+dx,y+dy
14                area+=dfs(nx,ny,island_id)
15            return area
16
17        island_id=2
18        for i in range(n):
19            for j in range(n):
20                if grid[i][j]==1:
21                    island[island_id]=dfs(i,j,island_id)
22                    island_id+=1
23
24        #step2: 以0为中心辐射,看看哪个0连接后岛屿面积最大 -max
25        def search(x,y):
26            area=0
27            seen=set()
28            for dx,dy in directions:
29                nx,ny= x+dx,y+dy
30                if 0<=nx<n and 0<=ny<n:
31                    island_id=grid[nx][ny]
32                    if island_id>1 and island_id not in seen:
33                        area+=island[island_id]
34                        seen.add(island_id)
35            return area
36
37        maxarea= max(island.values() or [0])
38        for i in range(n):
39            for j in range(n):
40                if grid[i][j]==0:
41                    maxarea=max(maxarea,search(i,j)+1)
42        return maxarea
43                    