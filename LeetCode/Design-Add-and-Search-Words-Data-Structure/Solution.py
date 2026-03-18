1class TrieNode:
2    def __init__(self):
3        self.children={}
4        self.is_end=False
5class WordDictionary:
6
7    def __init__(self):
8        self.root= TrieNode()
9
10    def addWord(self, word: str) -> None:
11        cur=self.root
12        for c in word:
13            if c not in cur.children:
14                cur.children[c] = TrieNode()
15            cur=cur.children[c]
16        cur.is_end=True
17
18    def search(self, word: str) -> bool:
19        n=len(word)
20        def helper(i,node):
21            if i==n:
22                return node.is_end
23            c=word[i]
24            if c==".":
25                for child in node.children.values():
26                    if  helper(i+1,child):
27                        return True
28                return False
29            else:
30                if c not in node.children:
31                    return False
32                else:
33                    return helper(i + 1, node.children[c])
34        return helper(0, self.root)
35
36
37# Your WordDictionary object will be instantiated and called as such:
38# obj = WordDictionary()
39# obj.addWord(word)
40# param_2 = obj.search(word)