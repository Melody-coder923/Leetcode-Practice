1class Solution:
2    def rotate(self, matrix: List[List[int]]) -> None:
3        n = len(matrix)
4        # Step 1: 转置矩阵
5        for i in range(n):
6            for j in range(i + 1, n):
7                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
8
9        # Step 2: 每一行反转
10        for row in matrix:
11            row.reverse()
12