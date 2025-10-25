class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        # 统计岛屿数量
        islands=[]
        directions=[(0,1),(1,0),(0,-1),(-1,0)]
        def dfs(i,j,path):
            if i<0 or j<0 or i>=m or j>=n or grid[i][j]!=1:
                return
            path.append((i,j))
            grid[i][j]=0
            for dx,dy in directions:
                nx,ny=i+dx,j+dy
                dfs(nx,ny,path)

        m,n=len(grid),len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    path=[]
                    dfs(i,j,path)
                    islands.append(path)
        
        shapes = set()

        for island in islands:
        # 找到岛屿最左上角作为原点
            min_x = min(x for x, _ in island)
            min_y = min(y for _, y in island)
        # 归一化岛屿形状
            normalized = tuple(sorted((x-min_x, y-min_y) for x,y in island))
            shapes.add(normalized)

        return len(shapes)

       