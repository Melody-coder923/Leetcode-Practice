1class TrieNode:
2    def __init__(self):
3        self.children={}
4        self.end=False
5class Trie:
6    def __init__(self):
7        self.root=TrieNode()
8    def insert(self, word: str) -> None:
9        cur=self.root
10        for c in word:
11            if c not in cur.children:
12                cur.children[c]=TrieNode()
13            cur=cur.children[c]
14        cur.end=True
15
16    def search(self, word: str) -> bool:
17        cur=self.root
18        for c in word:
19            if c not in cur.children:
20                return False
21            cur=cur.children[c]
22        return cur.end
23
24    def startsWith(self, prefix: str) -> bool:
25        cur=self.root
26        for c in prefix:
27            if c not in cur.children:
28                return False
29            cur=cur.children[c]
30        return True
31
32
33# Your Trie object will be instantiated and called as such:
34# obj = Trie()
35# obj.insert(word)
36# param_2 = obj.search(word)
37# param_3 = obj.startsWith(prefix)