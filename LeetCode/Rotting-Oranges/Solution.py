1class Solution:
2    def orangesRotting(self, grid: List[List[int]]) -> int:
3        m,n=len(grid),len(grid[0])
4        fresh=0
5        q=deque()
6        for i in range(m):
7            for j in range(n):
8                if grid[i][j]==1:
9                    fresh+=1
10                if grid[i][j]==2:
11                    q.append((i,j,0))
12        
13        if fresh==0:
14            return 0
15
16        directions=[(0,1),(0,-1),(1,0),(-1,0)]
17       
18        while q:
19            size=len(q)
20            for _ in range(size):
21                x,y,time=q.popleft()
22                for dx,dy in directions:
23                    nx,ny=x+dx,y+dy
24                    if 0<=nx<m and 0<=ny<n and grid[nx][ny]==1:
25                        grid[nx][ny]=2
26                        q.append((nx,ny,time+1))
27                        fresh-=1
28                        if fresh==0:
29                            return time+1
30        return -1
31
32