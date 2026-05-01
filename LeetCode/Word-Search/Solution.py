1class Solution:
2    def exist(self, board: List[List[str]], word: str) -> bool:
3        directions=[(0,1),(0,-1),(1,0),(-1,0)]
4        m,n= len(board),len(board[0])
5        
6
7        def dfs(i,j,k):
8            if i<0 or j<0 or i>=m or j>=n or board[i][j]==1 or board[i][j]!=word[k]:
9                return False
10            
11            if k==len(word)-1:
12                return True
13
14            temp=board[i][j]
15            board[i][j]=1
16            for dx,dy in directions:
17                if dfs(i+dx,j+dy,k+1):
18                    return True
19            board[i][j]=temp
20            return False
21
22        k=0
23        for i in range(m):
24            for j in range(n):
25                if board[i][j]==word[k]:
26                    if dfs(i,j,k):
27                        return True
28        return False