1class Solution:
2    def setZeroes(self, matrix: List[List[int]]) -> None:
3        """
4        Do not return anything, modify matrix in-place instead.
5        """
6        # 遍历 找0 然后 做记录哪些行和列受到影响
7        m,n=len(matrix),len(matrix[0])
8        firstrow=False
9        firstcol=False
10        for i in range(m):
11            if matrix[i][0]==0:
12                firstcol=True
13        for j in range(n):
14            if matrix[0][j]==0:
15                firstrow=True
16        for i in range(1,m):
17            for j in range(1,n):
18                if matrix[i][j]==0:
19                    matrix[i][0]=0
20                    matrix[0][j]=0
21        for i in range(1, m):
22            for j in range(1, n):
23                if matrix[i][0]==0 or matrix[0][j]==0:
24                    matrix[i][j]=0
25        if firstcol:
26            for i in range(m):
27                matrix[i][0]=0
28        if firstrow:
29            for i in range(n):
30                matrix[0][i]=0
31    
32