class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n,m=len(grid),len(grid[0])
        def dfs(x,y,island_id):
            if x<0 or y<0 or x>=n or y>=m or grid[x][y]!=1:
                return 0
            grid[x][y]=island_id
            return dfs(x+1,y,island_id)+dfs(x-1,y,island_id)+dfs(x,y+1,island_id)+dfs(x,y-1,island_id)+1
            
        island = {}
        island_id = 2
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    island[island_id] = dfs(i,j,island_id)
                    island_id += 1

        def search(x,y):
            seen=set()
            total=1
            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                nx, ny = x + dx, y + dy
                if 0<=nx<n and 0<=ny<m:
                    island_id = grid[nx][ny]
                    if island_id > 1 and island_id not in seen:
                        total+=island[island_id]
                        seen.add(island_id)
            return total
        maxarea = max(island.values() or [0])
        for i in range(n):
            for j in range(m):
                if grid[i][j]==0:
                    maxarea=max(maxarea,search(i,j))
        return maxarea

        