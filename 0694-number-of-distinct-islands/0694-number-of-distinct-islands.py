class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        # 相对坐标确定形状,sort tuple后, 放入set, 然后求Len(set)
        m,n=len(grid),len(grid[0])
        shapes=set()

        def dfs(i,j,x_base,y_base,shape):
            if i<0 or i>=m or j<0 or j>=n or grid[i][j]==0:
                return 
            grid[i][j]=0
            shape.append((i-x_base,j-y_base))

            dfs(i+1,j,x_base,y_base,shape)
            dfs(i-1,j,x_base,y_base,shape)
            dfs(i,j-1,x_base,y_base,shape)
            dfs(i,j+1,x_base,y_base,shape)


        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    shape=[]
                    dfs(i,j,i,j,shape)
                    shape.sort()
                    shapes.add(tuple(shape)) # set只能存哈希对象, 不可哈希的是list, dict, set
        return len(shapes)
