1class TrieNode:
2    def __init__(self):
3        self.children={}
4        self.is_end= False
5
6class Trie:
7    def __init__(self):
8        self.root= TrieNode()
9    def insert(self, word: str) -> None:
10        cur =self.root
11        for c in word:
12            if c not in cur.children:
13                cur.children[c]=TrieNode()
14            cur=cur.children[c]
15        cur.is_end=True
16        
17    def search(self, word: str) -> bool:
18        cur=self.root
19        for char in word:
20            if char not in cur.children:
21                return False
22            cur=cur.children[char]
23        return cur.is_end
24
25    def startsWith(self, prefix: str) -> bool:
26        cur=self.root
27        for char in prefix:
28            if char not in cur.children:
29                return False
30            cur=cur.children[char]
31        return True
32
33# Your Trie object will be instantiated and called as such:
34# obj = Trie()
35# obj.insert(word)
36# param_2 = obj.search(word)
37# param_3 = obj.startsWith(prefix)