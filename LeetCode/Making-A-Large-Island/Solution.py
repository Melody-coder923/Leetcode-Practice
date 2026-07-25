1class Solution:
2    def largestIsland(self, grid: List[List[int]]) -> int:
3        # step1: 求岛屿面积, 编号
4        n=len(grid)
5        island={} #key: island_id -> 面积
6        def cal(island_id,x,y):
7            if x<0 or x>=n or y<0 or y>=n or grid[x][y]!=1:
8                return 0
9            grid[x][y]=island_id
10            return cal(island_id,x+1,y)+cal(island_id,x-1,y)+cal(island_id,x,y+1)+cal(island_id,x,y-1)+1
11
12        island_id=2
13        for i in range(n):
14            for j in range(n):
15                if grid[i][j]==1:
16                    island[island_id]=cal(island_id,i,j)
17                    island_id+=1
18
19        # step2: 以0为中心辐射,看看哪个0连接后岛屿面积最大 -max
20        def search(x,y):
21            area=0
22            seen=set()
23            directions=[(1,0),(-1,0),(0,1),(0,-1)]
24            for dx,dy in directions:
25                nx,ny= x+dx,y+dy
26                if 0<=nx<n and 0<=ny<n:
27                    island_id=grid[nx][ny]
28                    if island_id>1 and island_id not in seen:
29                        area+=island[island_id]
30                        seen.add(island_id)
31            return area
32
33        maxarea= max(island.values() or [0])
34        for i in range(n):
35            for j in range(n):
36                if grid[i][j]==0:
37                    maxarea=max(maxarea,search(i,j)+1)
38        return maxarea