class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m,n=len(grid), len(grid[0])
        total=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    total+=4
                    if j<n-1 and grid[i][j+1]==1:
                        total-=2
                    if i <m-1 and grid[i+1][j]==1:
                        total-=2
        return total
