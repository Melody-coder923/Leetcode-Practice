1class Solution:
2    def rotate(self, matrix: List[List[int]]) -> None:
3        """
4        Do not return anything, modify matrix in-place instead.
5        """
6        n=len(matrix)
7        if n==1:
8            return matrix
9
10        for i in range(n):
11            for j in range(i, n):
12                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
13        
14        for row in matrix:
15            row.reverse()
16        
17        return matrix
18