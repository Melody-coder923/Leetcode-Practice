1class TrieNode:
2    def __init__(self):
3        self.children={} #key char : value TrieNode
4        self.isword=None
5        self.word=None
6
7
8class Solution:
9    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
10        #build Tries
11        root=TrieNode()
12        for word in words:
13            cur = root
14            for char in word:
15                if char not in cur.children:
16                    cur.children[char]=TrieNode()
17                cur=cur.children[char]
18            cur.isword=True
19            cur.word=word
20        m,n=len(board),len(board[0])
21        directions=[(0,-1),(0,1),(1,0),(-1,0)]
22        res=[]
23        def dfs(x,y,node):
24            if x < 0 or y < 0 or x >= m or y >= n:
25                return False
26
27            char=board[x][y] 
28            if char == "#":
29                return
30            
31            if char not in node.children:
32                return 
33            
34            nxt=node.children[char]
35            if nxt.isword:
36                res.append(nxt.word)
37                nxt.isword=False
38
39            board[x][y] = "#"
40
41            for dx,dy in directions:
42                nx,ny=x+dx,y+dy 
43                dfs(nx,ny,nxt)
44            board[x][y] = char
45
46            
47        for i in range(m):
48            for j in range(n):
49                if board[i][j] in root.children:      
50                    dfs(i,j,root)
51        return res