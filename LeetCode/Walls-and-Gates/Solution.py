1class Solution:
2    def wallsAndGates(self, rooms: List[List[int]]) -> None:
3        """
4        Do not return anything, modify rooms in-place instead.
5        """
6        m,n=len(rooms),len(rooms[0])
7        q=deque([])
8        INF=2147483647
9        #from treasure to nei
10        for i in range(m):
11            for j in range(n):
12                if rooms[i][j]==0: #tresure
13                    q.append(((i,j),0)) # 路径长
14    
15        
16        directions=[(0,1),(0,-1),(1,0),(-1,0)]
17        while q:
18            for _ in range(len(q)):
19                pos,path=q.popleft()
20                x,y=pos
21                for dx,dy in directions:
22                    nx,ny=x+dx,y+dy
23                    if 0<=nx<m and 0<=ny<n and rooms[nx][ny]==INF:
24                        rooms[nx][ny]=path+1
25                        q.append(((nx, ny), path + 1))
26    
27                        
28
29
30       