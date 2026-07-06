1class Solution:
2    def wallsAndGates(self, rooms: List[List[int]]) -> None:
3        """
4        Do not return anything, modify rooms in-place instead.
5        """
6        m,n=len(rooms),len(rooms[0])
7        INF=2147483647
8        q=deque()
9        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
10        for i in range(m):
11            for j in range(n):
12                if rooms[i][j]== 0:
13                    q.append((i,j,0))
14        
15        while q:
16            size=len(q)
17            for _ in range(size):
18                x,y,level= q.popleft()
19                for dx,dy in directions:
20                    nx,ny=x+dx,y+dy
21                    if 0<=nx<m and 0<=ny<n and rooms[nx][ny]==INF:
22                        q.append((nx,ny,level+1))
23                        rooms[nx][ny]=level+1
24