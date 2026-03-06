1class Solution:
2    def orangesRotting(self, grid: List[List[int]]) -> int:
3        m,n=len(grid),len(grid[0])
4        fresh=0
5        q=deque()
6        for i in range(m):
7            for j in range(n):
8                if grid[i][j]==1:
9                    fresh+=1
10                elif grid[i][j]==2:
11                    q.append((i,j))
12        
13        if fresh==0:
14            return 0
15        directions=[[0,1],[0,-1],[1,0],[-1,0]]
16        time=0
17        while q and fresh>0:
18            for _ in range(len(q)):
19                x, y = q.popleft()
20                for dx,dy in directions:
21                    nx,ny=x+dx,y+dy
22                    if 0<=nx<m and 0<=ny<n and grid[nx][ny]==1:
23                        fresh-=1
24                        grid[nx][ny]=2
25                        q.append((nx,ny))         
26            time+=1
27        return time if fresh == 0 else -1
28