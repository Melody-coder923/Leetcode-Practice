1class Solution:
2    def wallsAndGates(self, rooms: List[List[int]]) -> None:
3        """
4        Do not return anything, modify rooms in-place instead.
5        """
6        INF=2**31-1
7        m,n=len(rooms),len(rooms[0])
8        q=deque()
9        for i in range(m):
10            for j in range(n):
11                if rooms[i][j]==0:
12                    q.append((i,j,0))
13        directions=[(1,0),(-1,0),(0,1),(0,-1)]
14        while q:
15            size=len(q)
16            for _ in range(size):
17                x,y,dis=q.popleft()
18                for dx,dy in directions:
19                    nx,ny=x+dx,y+dy
20                    if 0<=nx<m and 0<=ny<n and rooms[nx][ny]==INF:
21                        q.append((nx,ny,dis+1))
22                        rooms[nx][ny]=dis+1
23        