1class Solution:
2    def setZeroes(self, matrix: List[List[int]]) -> None:
3        """
4        Do not return anything, modify matrix in-place instead.
5        """
6        #row[0] col[0] 先检查存flag
7        #用row[0] col[0]做标记
8
9        m,n=len(matrix),len(matrix[0])
10        flag_col=False
11        flag_row=False
12
13        for i in range(m):
14            if matrix[i][0]==0:
15                flag_col=True 
16        for j in range(n):
17            if matrix[0][j]==0:
18                flag_row=True 
19        
20        for i in range(1,m):
21            for j in range(1,n):
22                if matrix[i][j]==0:
23                    matrix[0][j]=0
24                    matrix[i][0]=0
25        
26
27        for i in range(1,m):
28            for j in range(1,n):
29                if matrix[0][j]==0:
30                    matrix[i][j]=0
31                if matrix[i][0]==0:
32                    matrix[i][j]=0
33
34        if flag_col:    
35            for i in range(m):
36                matrix[i][0]=0
37        if flag_row:
38            for j in range(n):
39                matrix[0][j]=0
40