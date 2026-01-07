class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        if m<3 or n<3:
            return 0

        def helper(i,j):
            # 中间是5
            if grid[i+1][j+1]!=5:
                return False
            
            # collection set==set(1-9)
            compare=set(i for i in range(1,10))
            collection = set([
                grid[i][j], grid[i][j+1], grid[i][j+2],
                grid[i+1][j], grid[i+1][j+1], grid[i+1][j+2],
                grid[i+2][j], grid[i+2][j+1], grid[i+2][j+2]
            ])     #set里面只能是一个对象
            if compare != collection:
                return False

            # 每一行,每一列,每个对角线是15
            if (
                grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2] != 15 or
                grid[i][j+2] + grid[i+1][j+1] + grid[i+2][j] != 15 or
                grid[i][j] + grid[i][j+1] + grid[i][j+2] != 15 or
                grid[i+1][j] + grid[i+1][j+1] + grid[i+1][j+2] != 15 or
                grid[i+2][j] + grid[i+2][j+1] + grid[i+2][j+2] != 15 or
                grid[i][j] + grid[i+1][j] + grid[i+2][j] != 15 or
                grid[i][j+1] + grid[i+1][j+1] + grid[i+2][j+1] != 15 or
                grid[i][j+2] + grid[i+1][j+2] + grid[i+2][j+2] != 15
                ): #要加括号
                return False
            return True

        count=0
        for i in range(m-2):
            for j in range(n-2):
                if helper(i,j):
                    count+=1
        return count
      