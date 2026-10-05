1class Solution:
2    def wallsAndGates(self, rooms: list[list[int]]) -> None:
3        """
4        Do not return anything, modify rooms in-place instead.
5        """
6        INF=2147483647
7        m,n=len(rooms),len(rooms[0])
8        directions=[(1,0),(-1,0),(0,1),(0,-1)]
9
10        q=deque()
11        for i in range(m):
12            for j in range(n):
13                if rooms[i][j]==0:
14                    q.append((i,j,0))
15        
16
17        while q:
18            size=len(q)
19            for _ in range(size):
20                x,y,step=q.popleft()
21                if rooms[x][y]==INF:
22                    rooms[x][y]=step
23
24                for dx,dy in directions:
25                    nx,ny=x+dx,y+dy
26                    if 0<=nx<m and 0<=ny<n and rooms[nx][ny]==INF:
27                        q.append((nx,ny,step+1))
28            