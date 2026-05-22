1class TrieNode:
2    def __init__(self):
3        self.children={}
4        self.is_end= False
5       
6class Trie:
7    def __init__(self):
8        self.root= TrieNode()
9
10    def insert(self, word: str) -> None:
11        cur=self.root
12        for char in word:
13            if char not in cur.children:
14                cur.children[char]=TrieNode()
15            cur=cur.children[char]
16        cur.is_end=True
17
18    def search(self, word: str) -> bool:
19        cur=self.root
20        for char in word:
21            if char not in cur.children:
22                return False
23            cur=cur.children[char]
24        return cur.is_end
25     
26    def startsWith(self, prefix: str) -> bool:
27        cur=self.root
28        for char in prefix:
29            if char not in cur.children:
30                return False
31            cur=cur.children[char]
32        return True
33        
34# Your Trie object will be instantiated and called as such:
35# obj = Trie()
36# obj.insert(word)
37# param_2 = obj.search(word)
38# param_3 = obj.startsWith(prefix)