class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        # 判断形状
        # 找出岛屿,并且把岛屿内部坐标排序, 再存进set->len(set)

        # 前置工具, 搜集岛屿坐标
        def dfs(x,y,base_x,base_y,shape):
            if x<0 or x>=m or y<0 or y>=n or grid[x][y]!=1:
                return
            shape.append((x-base_x,y-base_y))
            grid[x][y]=0
            dfs(x+1,y,base_x,base_y,shape)
            dfs(x-1,y,base_x,base_y,shape)
            dfs(x,y+1,base_x,base_y,shape)
            dfs(x,y-1,base_x,base_y,shape)

        # step1: 找岛屿, 存坐标
        m,n=len(grid),len(grid[0])
        islands=set()
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    shape=[]
                    dfs(i,j,i,j,shape) 
                    #step2: 排序,放进set
                    shape.sort()
                    islands.add(tuple(shape))
        return len(islands)


        