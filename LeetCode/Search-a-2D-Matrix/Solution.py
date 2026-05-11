1class Solution:
2    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
3        if not matrix or not matrix[0]:
4            return False
5        m, n = len(matrix), len(matrix[0])
6        left, right = 0, m * n - 1
7        while left <= right:
8            mid = (left + right) // 2
9            # 将一维索引映射到二维矩阵
10            row, col = divmod(mid, n)
11            val = matrix[row][col]
12            if val == target:
13                return True
14            elif val < target:
15                left = mid + 1
16            else:
17                right = mid - 1
18        return False