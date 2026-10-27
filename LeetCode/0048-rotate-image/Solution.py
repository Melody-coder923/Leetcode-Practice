class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
             0,1  0,2
        1,0 
        2,0   
        """
        n=len(matrix)
        # reverse in diagonal
        for i in range(n):
            for j in range(i):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        
        # reverse in row
        for row in matrix:
            row.reverse()
        
        return matrix
