1class Solution:
2    def wallsAndGates(self, rooms: List[List[int]]) -> None:
3        """
4        Do not return anything, modify rooms in-place instead.
5        """
6        if not rooms or not rooms[0]:
7            return 
8
9        INF=2147483647
10        m,n=len(rooms),len(rooms[0])
11        directions= [(-1,0),(1,0),(0,-1),(0,1)]
12        q=deque()
13       
14        for i in range(m):
15            for j in range(n):
16                if rooms[i][j]==0:
17                    q.append((i,j))
18        while q:
19            x,y=q.popleft()
20            for dx,dy in directions:
21                nx,ny=x+dx,y+dy
22                if 0<=nx<m and 0<=ny<n and rooms[nx][ny]==INF:
23                    rooms[nx][ny] = rooms[x][y] + 1
24                    q.append((nx,ny))