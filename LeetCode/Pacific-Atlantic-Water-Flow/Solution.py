1class Solution:
2    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
3        m,n=len(heights),len(heights[0])
4        pacific = set()
5        atlantic = set()
6        directions=[(-1,0),(1,0),(0,-1),(0,1)]
7        
8        def dfs(x,y,visited):
9            visited.add((x,y))
10            for dx,dy in directions:
11                nx,ny=x+dx,y+dy
12                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited and heights[nx][ny] >= heights[x][y]:
13                    dfs(nx, ny, visited)
14
15        for i in range(n):
16            if (0, i) not in pacific:
17                dfs(0, i, pacific)
18            if (m - 1, i) not in atlantic:
19                dfs(m - 1, i, atlantic)
20
21        for i in range(m):
22            if (i, 0) not in pacific:
23                dfs(i, 0, pacific)
24            if (i, n - 1) not in atlantic:
25                dfs(i, n - 1, atlantic)
26        return list(pacific & atlantic)