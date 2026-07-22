1class Solution:
2    def solveNQueens(self, n: int) -> List[List[str]]:
3        res=[]
4        board=["."*n for _ in range(n)]
5        def backtrack(row):
6            if row==n:
7                res.append(board[:])
8                return 
9            
10            for col in range(n):
11                if valid(board,row,col):
12                    board[row]=board[row][:col]+"Q"+board[row][col+1:]
13                    backtrack(row+1)
14                    board[row]=board[row][:col]+"."+board[row][col+1:]
15
16
17        def valid(board,row,col):
18            for i in range(row):
19                if board[i][col]=="Q":
20                    return False
21                
22            i,j=row-1,col-1
23            while i>=0 and j>=0:
24                if board[i][j]=="Q":
25                    return False
26                i-=1
27                j-=1
28        
29            i,j=row-1,col+1
30            while i>=0 and j<n:
31                if board[i][j]=="Q":
32                    return False
33                i-=1
34                j+=1
35            return True
36
37
38        backtrack(0)
39        return res