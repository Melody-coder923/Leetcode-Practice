1class Solution:
2    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
3        m,n=len(matrix),len(matrix[0])
4        if not matrix or not matrix[0]:
5            return []
6
7        res=[]
8        l,r=0,n-1
9        top,bottom=0,m-1
10        while l<=r and top<=bottom:
11            #l->r
12            for i in range(l,r+1):
13                res.append(matrix[top][i])
14            top+=1
15            #top->bottom
16            for i in range(top,bottom+1):
17                res.append(matrix[i][r])
18            r-=1
19            if top<=bottom:
20            #r->l
21                for i in range(r,l-1,-1):
22                    res.append(matrix[bottom][i])
23                bottom-=1
24            if l<=r:
25            #bottom->top
26                for i in range(bottom,top-1,-1):
27                    res.append(matrix[i][l])
28                l+=1
29        return res
30      
31
32