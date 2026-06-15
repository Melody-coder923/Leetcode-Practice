1class TriesNode:
2    def __init__(self):
3        self.children={}
4        self.word=None
5
6class Solution:
7    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
8        root=TriesNode()
9        for word in words:
10            cur=root
11            for c in word:
12                if c not in cur.children:
13                    cur.children[c]=TriesNode()
14                cur=cur.children[c]
15            cur.word=word
16        
17        directions=[(0,-1),(0,1),(-1,0),(1,0)]
18        res=[]
19        m,n=len(board),len(board[0])
20        def dfs(i,j,node):
21            if i<0 or j<0 or i>=m or j>=n or board[i][j]=="#":
22                return
23            char=board[i][j]
24            if char not in node.children:
25                return 
26            
27            node = node.children[char]
28            if node.word:
29                res.append(node.word)
30                node.word=None
31           
32            board[i][j]="#"
33            for di,dj in directions:
34                ni,nj=i+di,j+dj
35                if 0<=ni<m and 0<=nj<n and board[ni][nj] in node.children:
36                    dfs(ni,nj,node)
37            board[i][j]=char
38            return res
39        cur=root
40        for i in range(m):
41            for j in range(n):
42                dfs(i,j,cur)
43        return res
44        