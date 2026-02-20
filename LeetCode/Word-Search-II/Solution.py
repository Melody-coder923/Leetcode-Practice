1from typing import List
2
3class TrieNode:
4    def __init__(self):
5        self.children = {}      # char -> TrieNode
6        self.is_word = None     # 存完整单词
7        self.is_end = False     # 是否单词结尾
8
9class Trie:
10    def __init__(self):
11        self.root = TrieNode()
12
13    def insert(self, word):
14        cur = self.root
15        for char in word:
16            if char not in cur.children:
17                cur.children[char] = TrieNode()
18            cur = cur.children[char]   # ✅ 关键修复
19        cur.is_end = True
20        cur.is_word = word
21
22
23class Solution:
24    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
25        trie = Trie()
26        for word in words:
27            trie.insert(word)
28
29        m, n = len(board), len(board[0])
30        directions = [(-1,0), (1,0), (0,-1), (0,1)]
31        visited = [[False]*n for _ in range(m)]
32        res = []
33
34        def dfs(x, y, node):
35            if x < 0 or x >= m or y < 0 or y >= n or visited[x][y]:
36                return
37            if board[x][y] not in node.children:
38                return
39
40            visited[x][y] = True
41            node = node.children[board[x][y]]
42
43            if node.is_end:
44                res.append(node.is_word)
45                node.is_end = False   # ✅ 去重关键
46
47            for dx, dy in directions:
48                dfs(x + dx, y + dy, node)
49
50            visited[x][y] = False    # 回溯
51
52        for i in range(m):
53            for j in range(n):
54                dfs(i, j, trie.root)
55
56        return res
57