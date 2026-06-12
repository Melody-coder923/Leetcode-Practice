1class TrieNode:
2    def __init__(self):
3        self.children = {}
4        self.word = None
5
6class Solution:
7    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
8        root=TrieNode()
9        for word in words:
10            cur=root
11            for char in word:
12                if char not in cur.children:
13                    cur.children[char]=TrieNode()
14                cur=cur.children[char]
15            cur.word = word
16        res=[]
17        m,n=len(board),len(board[0])
18        directions = [(1,0), (-1,0), (0,1), (0,-1)]
19        def dfs(i,j,node):
20            if i<0 or j<0 or i>=m or j>=n or board[i][j]=="#" or board[i][j] not in node.children:
21                return
22            char=board[i][j]
23            node = node.children[char]
24            if node.word:
25                res.append(node.word)
26                node.word=None
27                
28            board[i][j]="#"
29            for dx,dy in directions:
30                ni,nj=i+dx,j+dy
31                if 0<=ni<m and 0<=nj<n and board[ni][nj] in node.children:
32                    dfs(ni,nj,node)
33            board[i][j]=char
34
35        cur=root
36        for i in range(m):
37            for j in range(n):
38                dfs(i, j, root)
39        return res
40        