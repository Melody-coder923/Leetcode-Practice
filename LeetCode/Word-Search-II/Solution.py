1class TrieNode:
2    def __init__(self):
3        self.children={}
4        self.end=False
5        self.word=None
6
7class Solution:
8    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
9        root=TrieNode()
10        for word in words:
11            cur=root
12            for c in word:
13                if c not in cur.children:
14                    cur.children[c]=TrieNode()
15                cur=cur.children[c]
16            cur.end=True
17            cur.word=word
18        
19     
20        directions=[(0,-1),(0,1),(-1,0),(1,0)]
21        res=[]
22        m,n=len(board),len(board[0])
23        def dfs(i,j,node):
24            if i<0 or j<0 or i>=m or j>=n or board[i][j]=="#":
25                return
26            char=board[i][j]
27            if char not in node.children:
28                return 
29            
30            node = node.children[char]
31            if node.word:
32                res.append(node.word)
33                node.word=None
34           
35            board[i][j]="#"
36            for di,dj in directions:
37                ni,nj=i+di,j+dj
38                if 0<=ni<m and 0<=nj<n and board[ni][nj] in node.children:
39                    dfs(ni,nj,node)
40            board[i][j]=char
41            return res
42
43        cur=root
44        for i in range(m):
45            for j in range(n):
46                dfs(i,j,cur)
47        return res