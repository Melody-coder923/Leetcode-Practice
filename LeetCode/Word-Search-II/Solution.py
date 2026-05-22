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
20            if i<0 or j<0 or i>=m or j>=n:
21                return
22            char = board[i][j]
23            if char == "#" or char not in node.children:
24                return
25
26            node = node.children[char]
27            if node.word:
28                res.append(node.word)
29                node.word = None
30
31            board[i][j] = "#"
32
33            for dx, dy in directions:
34                dfs(i + dx, j + dy, node)           
35            board[i][j] = char
36        
37        cur=root
38        for i in range(m):
39            for j in range(n):
40                dfs(i, j, root)
41        return res
42        