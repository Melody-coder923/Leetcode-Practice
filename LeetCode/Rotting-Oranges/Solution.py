1class Solution:
2    def orangesRotting(self, grid: List[List[int]]) -> int:
3        m,n=len(grid),len(grid[0])
4        fresh=0
5        q=deque()
6        time=0
7        directions = [(1,0), (-1,0), (0,1), (0,-1)]
8        for i in range(m):
9            for j in range(n):
10                if grid[i][j]==1:
11                    fresh+=1
12                elif grid[i][j]==2:
13                    q.append((i,j,time))
14        if fresh == 0:
15            return 0
16        while q:
17            size=len(q)
18            for _ in range(size):
19                x,y,time=q.popleft()
20                for dx,dy in directions:
21                    nx, ny = x + dx, y + dy
22                    if 0<=nx<m and 0<=ny<n and grid[nx][ny]==1:
23                        grid[nx][ny] = 2
24                        q.append((nx,ny,time+1))
25                        fresh-=1
26                        if fresh == 0:
27                            return time + 1
28        return -1