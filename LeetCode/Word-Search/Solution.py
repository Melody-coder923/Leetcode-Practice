1class Solution:
2    def exist(self, board: List[List[str]], word: str) -> bool:
3        m,n=len(board),len(board[0])
4        if len(word)> m*n:
5            return False
6        
7        directions=[(1,0),(-1,0),(0,1),(0,-1)]
8        def dfs(x,y,index):
9            if x<0 or x>=m or y<0 or y>=n or board[x][y]==1 or board[x][y]!=word[index]:
10                return False
11            if index==len(word)-1:
12                return True
13            temp=board[x][y]
14            board[x][y]=1
15            for dx,dy in directions:
16                nx,ny=x+dx, y+dy
17                if dfs(nx, ny, index + 1):
18                    return True
19            board[x][y]=temp
20        
21        for i in range(m):
22            for j in range(n):
23                if board[i][j]==word[0]:
24                    if dfs(i,j,0):
25                        return True
26        return False
27
28