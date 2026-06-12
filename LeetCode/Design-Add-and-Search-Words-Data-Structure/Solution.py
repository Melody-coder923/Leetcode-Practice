1class TrieNode:
2    def __init__(self):
3        self.children={}
4        self.end=False
5
6class WordDictionary:
7    def __init__(self):
8        self.root=TrieNode()
9
10    def addWord(self, word: str) -> None:
11        cur=self.root
12        for c in word:
13            if c not in cur.children:
14                cur.children[c]=TrieNode()
15            cur=cur.children[c]
16        cur.end=True
17
18    def search(self, word: str) -> bool:
19        def dfs(i,node):
20            if i==len(word):
21                return node.end
22            c=word[i]
23            if c != ".":
24                if c not in node.children:
25                    return False
26                return dfs(i + 1, node.children[c]) 
27            for child in node.children.values():
28                if dfs(i + 1, child):
29                    return True
30            return False
31        return dfs(0,self.root)
32
33# Your WordDictionary object will be instantiated and called as such:
34# obj = WordDictionary()
35# obj.addWord(word)
36# param_2 = obj.search(word)