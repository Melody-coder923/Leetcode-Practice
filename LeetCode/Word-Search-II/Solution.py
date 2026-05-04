1class TrieNode:
2    def __init__(self):
3        self.children={}
4        self.is_end=False
5        self.word= None
6
7class Solution:
8    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
9        root=TrieNode()
10        for word in words:
11            curr=root
12            for char in word:
13                if char not in curr.children:
14                    curr.children[char]=TrieNode()
15                curr=curr.children[char]
16            curr.is_end=True
17            curr.word=word
18        
19        m,n=len(board),len(board[0])
20        directions=[(1,0),(-1,0),(0,1),(0,-1)]
21        visited = [[False]*n for _ in range(m)]
22        res=[]
23        def dfs(x,y,node):
24            if x<0 or y<0 or x>=m or y>=n or visited[x][y]:
25                return
26            char=board[x][y]
27            if char not in node.children:
28                return 
29            visited[x][y] = True
30            node = node.children[char]
31            if node.is_end:
32                res.append(node.word)
33                node.is_end=False 
34
35            for dx,dy in directions:
36                nx,ny=x+dx,y+dy
37                dfs(nx,ny,node)
38            visited[x][y] = False 
39            
40
41        
42        for i in range(m):
43            for j in range(n):
44                dfs(i,j,root)
45        return res