1class Solution:
2    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
3        m,n=len(matrix),len(matrix[0]) #3,4
4        l,r=0, m*n-1 
5        while l<=r:
6            mid=l+(r-l)//2
7            x=mid//n    #5//3=1
8            y=mid%n  #5%4=1
9
10            if matrix[x][y]==target:
11                return True
12            elif matrix[x][y]>target:
13                r=mid-1
14            else:
15                l=mid+1
16        return False