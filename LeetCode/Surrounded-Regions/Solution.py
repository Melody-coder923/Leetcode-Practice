1class Solution:
2    def solve(self, board: List[List[str]]) -> None:
3        """
4        Do not return anything, modify board in-place instead.
5        """
6        if not board or not board[0]:
7            return
8        m,n=len(board),len(board[0])
9        directions=[(0,1),(0,-1),(1,0),(-1,0)]
10        def dfs(x,y):
11            if x<0 or y<0 or x>=m or y>=n or board[x][y]!="O":
12                return 
13            board[x][y]="#"
14            for dx,dy in directions:
15                nx,ny=x+dx,y+dy
16                dfs(nx,ny)
17            
18        for i in range(m):
19            if board[i][0]=="O":
20                dfs(i,0)
21            if board[i][n-1]=="O":
22                dfs(i,n-1)
23        
24        for j in range(n):
25            if board[0][j]=="O":
26                dfs(0,j)
27            if board[m-1][j]=="O":
28                dfs(m-1,j)
29        
30        for i in range(m):
31            for j in range(n):
32                if board[i][j]=="O":
33                    board[i][j]="X"
34                if board[i][j]=="#":
35                    board[i][j]="O"
36        
37            
38
39