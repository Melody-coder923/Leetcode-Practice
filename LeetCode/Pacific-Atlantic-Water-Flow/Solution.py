1class Solution:
2    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
3        m,n=len(heights),len(heights[0])
4        directions = [(1,0), (-1,0), (0,1), (0,-1)]
5        def dfs(x,y,visited):
6            if (x,y) in visited:
7                return
8            visited.add((x,y))
9            for dx,dy in directions:
10                nx,ny=x+dx,y+dy
11                if 0 <= nx < m and 0 <= ny < n and heights[nx][ny] >= heights[x][y]:
12                    dfs(nx,ny,visited)
13        a=set()
14        p=set()
15        for i in range(m):
16            dfs(i,0,p)
17            dfs(i,n-1,a)
18        for j in range(n):
19            dfs(0,j,p)
20            dfs(m-1,j,a)
21
22        return [[x, y] for x, y in p & a]
23        
24            