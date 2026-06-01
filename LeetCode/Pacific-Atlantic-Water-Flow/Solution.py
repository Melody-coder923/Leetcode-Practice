1class Solution:
2    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
3        m,n=len(heights),len(heights[0])
4        directions = [(1,0), (-1,0), (0,1), (0,-1)]
5        def dfs(i,j,visited):
6            if (i, j) in visited:
7                return
8            visited.add((i,j))
9            for dx,dy in directions:
10                ni,nj=i+dx,j+dy
11                if 0<=ni<m and 0<=nj<n and heights[ni][nj]>=heights[i][j]:
12                    dfs(ni,nj,visited)
13
14        p_set=set()
15        a_set=set()
16        for i in range(m):
17            dfs(i, 0, p_set)        # Pacific 左边
18            dfs(i, n - 1, a_set)    # Atlantic 右边
19        
20        for j in range(n):
21            dfs(0, j, p_set)        # Pacific 上边
22            dfs(m - 1, j, a_set)    # Atlantic 下边
23        
24        res= p_set&a_set
25        return [list(cell) for cell in res]