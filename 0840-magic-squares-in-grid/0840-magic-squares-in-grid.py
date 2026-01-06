class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0
        for i in range(m - 2):
            for j in range(n - 2):
                # 剪枝 1：中心必须是 5
                if grid[i+1][j+1] != 5:
                    continue

                nums = {
                    grid[i][j], grid[i][j+1], grid[i][j+2],
                    grid[i+1][j], grid[i+1][j+1], grid[i+1][j+2],
                    grid[i+2][j], grid[i+2][j+1], grid[i+2][j+2],
                }

                # 剪枝 2：必须是 1~9
                if nums != set(range(1, 10)):
                    continue

                # 剪枝 3：检查和
                if (
                    grid[i][j] + grid[i][j+1] + grid[i][j+2] == 15 and
                    grid[i+1][j] + grid[i+1][j+1] + grid[i+1][j+2] == 15 and
                    grid[i+2][j] + grid[i+2][j+1] + grid[i+2][j+2] == 15 and
                    grid[i][j] + grid[i+1][j] + grid[i+2][j] == 15 and
                    grid[i][j+1] + grid[i+1][j+1] + grid[i+2][j+1] == 15 and
                    grid[i][j+2] + grid[i+1][j+2] + grid[i+2][j+2] == 15 and
                    grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2] == 15 and
                    grid[i][j+2] + grid[i+1][j+1] + grid[i+2][j] == 15
                ):
                    res += 1

        return res


        