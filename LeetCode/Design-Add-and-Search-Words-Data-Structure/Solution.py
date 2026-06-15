1class TriesNode:
2    def __init__(self):
3        self.children={}
4        self.end=False
5class WordDictionary:
6    def __init__(self):
7        self.root=TriesNode()
8    def addWord(self, word: str) -> None:
9        cur=self.root
10        for c in word:
11            if c not in cur.children:
12                cur.children[c]=TriesNode()
13            cur=cur.children[c]
14        cur.end=True
15
16    def search(self, word: str) -> bool:
17        def dfs(i,node):
18            if i==len(word):
19                return node.end
20            c=word[i]
21            if c!=".":
22                if c not in node.children:
23                    return False
24                return dfs(i + 1, node.children[c])
25            else:
26                for child in node.children.values():
27                    if dfs(i+1,child):
28                        return True
29                return False
30        return dfs(0,self.root)
31# Your WordDictionary object will be instantiated and called as such:
32# obj = WordDictionary()
33# obj.addWord(word)
34# param_2 = obj.search(word)