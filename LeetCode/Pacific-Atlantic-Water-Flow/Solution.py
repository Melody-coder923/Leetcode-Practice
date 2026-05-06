1class Solution:
2    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
3        m,n=len(heights),len(heights[0])
4        directions = [(1,0), (-1,0), (0,1), (0,-1)]
5        def dfs(i,j,visited):
6            if (i, j) in visited:
7                return
8            visited.add((i, j))
9            for dx,dy in directions:
10                nx,ny=i+dx,j+dy
11                if 0 <= nx < m and 0 <= ny < n and heights[nx][ny] >= heights[i][j]:
12                    dfs(nx, ny, visited)
13
14        
15        #从atlantic扩散一圈
16        #从pacific扩散一圈
17        a=set()
18        p=set()
19        for i in range(m):
20            dfs(i,n-1,a)
21            dfs(i,0,p)
22        for j in range(n):
23            dfs(m-1,j,a)
24            dfs(0,j,p)
25        #看交集？
26        return list(a & p)
27        