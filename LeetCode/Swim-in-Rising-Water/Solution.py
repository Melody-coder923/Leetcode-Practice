1class Solution:
2    def swimInWater(self, grid: List[List[int]]) -> int:
3        m, n = len(grid), len(grid[0]) 
4        directions = [(1,0), (-1,0), (0,1), (0,-1)]
5        visited={(0,0)}
6        heap=[]
7        heapq.heappush(heap,(grid[0][0],0,0))
8        while heap:
9            max_level,x,y =heapq.heappop(heap)
10            if x == m - 1 and y == n - 1: 
11                return max_level
12            for dx,dy in directions:
13                nx,ny=x+dx,y+dy
14                if 0<=nx<m and 0<=ny<n and (nx, ny) not in visited:
15                    new_max=max(max_level,grid[nx][ny])
16                    heapq.heappush(heap,(new_max,nx,ny))
17                    visited.add((nx, ny))
18