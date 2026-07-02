1class Solution:
2    def exist(self, board: List[List[str]], word: str) -> bool:
3        m,n=len(board),len(board[0])
4        directions = [(0,1), (0,-1), (1,0), (-1,0)]
5        def dfs(i,j,idx):
6            if i<0 or j<0 or i>=m or j>=n or board[i][j]!=word[idx]:
7                return False
8            if board[i][j]=="#":
9                return False
10            if idx==len(word)-1:
11                return True
12            
13            temp=board[i][j]
14            board[i][j]="#"
15            for di,dj in directions:
16                ni,nj=i+di,j+dj
17                if dfs(ni,nj,idx+1):
18                    board[i][j] =temp
19                    return True
20            board[i][j]=temp
21            return False
22
23        for i in range(m):
24            for j in range(n):
25                if board[i][j]==word[0]:
26                    if dfs(i,j,0):
27                        return True
28        return False