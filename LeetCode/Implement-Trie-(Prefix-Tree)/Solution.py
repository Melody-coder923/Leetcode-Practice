1class TrieNode:
2    def __init__(self):
3        self.children={}
4        self.end=False
5
6class Trie:
7    def __init__(self):
8        self.root=TrieNode()
9
10    def insert(self, word: str) -> None:
11        cur=self.root
12        for c in word:
13            if c not in cur.children:
14                cur.children[c]=TrieNode()
15            cur=cur.children[c]
16        cur.end=True
17
18    def search(self, word: str) -> bool:
19        cur=self.root
20        for c in word:
21            if c not in cur.children:
22                return False
23            cur=cur.children[c]
24        return cur.end
25
26    def startsWith(self, prefix: str) -> bool:
27        cur=self.root
28        for c in prefix:
29            if c not in cur.children:
30                return False
31            cur=cur.children[c]
32        return True
33        
34
35
36# Your Trie object will be instantiated and called as such:
37# obj = Trie()
38# obj.insert(word)
39# param_2 = obj.search(word)
40# param_3 = obj.startsWith(prefix)