1class Solution:
2    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
3        top,down=0,len(matrix)-1
4        l,r=0,len(matrix[0])-1
5        res=[]
6        while l<=r and top<=down:
7            for j in range(l,r+1):
8                res.append(matrix[top][j])
9            top+=1
10            for i in range(top,down+1):
11                res.append(matrix[i][r])
12            r-=1
13            if top <= down:
14                for j in range(r,l-1,-1):
15                    res.append(matrix[down][j])
16                down-=1
17            if l <= r:
18                for i in range(down,top-1,-1):
19                    res.append(matrix[i][l])
20                l+=1
21        
22        return res
23
24            
25
26