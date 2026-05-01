1class Solution:
2    def exist(self, board: List[List[str]], word: str) -> bool:
3        m,n=len(board),len(board[0])
4        directions=[(-1,0),(0,1),(1,0),(0,-1)]
5        def dfs(i,j,idx):
6            if word[idx]!=board[i][j]:
7                return False
8            if idx==len(word)-1:
9                return True
10            temp=board[i][j]
11            board[i][j]=1
12            for dx,dy in directions:
13                nx,ny=dx+i,dy+j
14                if 0<=nx<m and 0<=ny<n and board[nx][ny]!=1:
15                    if dfs(nx,ny,idx+1):
16                        return True
17            board[i][j]=temp
18            return False
19        idx=0
20        for i in range(m):
21            for j in range(n):
22                if board[i][j]==word[idx]:
23                    if dfs(i,j,idx):
24                        return True
25        return False