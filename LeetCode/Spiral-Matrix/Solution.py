1class Solution:
2    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
3        if not matrix or not matrix[0]:
4            return []
5
6        left,right=0,len(matrix[0])-1
7        top,bottom=0,len(matrix)-1
8        res=[]
9        while left<=right and top<=bottom:
10            for i in range(left,right+1):
11                res.append(matrix[top][i])
12            top+=1
13
14            for i in range(top,bottom+1):
15                res.append(matrix[i][right])
16            right-=1
17
18            if top<=bottom:
19                for i in range(right,left-1,-1):
20                    res.append(matrix[bottom][i])
21                bottom-=1
22            
23            if left<=right: 
24                for i in range(bottom, top-1,-1):
25                    res.append(matrix[i][left])
26                left+=1
27
28        return res           
29