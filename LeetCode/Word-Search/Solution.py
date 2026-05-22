1class Solution:
2    def exist(self, board: List[List[str]], word: str) -> bool:
3        directions=[(0,1),(0,-1),(1,0),(-1,0)]
4        def backtrack(i,j,idx):
5            if i<0 or j<0 or i>=m or j>=n or board[i][j]==1:
6                return False
7            if board[i][j]!=word[idx]:
8                return False
9            if idx==len(word)-1:
10                return True
11            temp=board[i][j]
12            board[i][j]=1
13            for dx,dy in directions:
14                nx,ny=i+dx,j+dy
15                if backtrack(nx,ny,idx+1):
16                    return True
17            board[i][j]=temp
18            return False
19
20        m,n=len(board),len(board[0])
21        idx=0
22        for i in range(m):
23            for j in range(n):
24                if board[i][j]==word[idx]:
25                    if backtrack(i,j,idx):
26                        return True
27        return False