1class TrieNode():
2    def __init__(self):
3        self.children={} # char->node
4        self.is_end=False
5# 方便查找-> 存进去 -> container -> tries (node)
6class WordDictionary:
7    def __init__(self):
8        self.root= TrieNode()
9
10    def addWord(self, word: str) -> None:
11        cur=self.root #b a d
12        for c in word:
13            if c not in cur.children:
14                cur.children[c]=TrieNode()
15            cur=cur.children[c]
16        cur.is_end=True
17        
18    def search(self, word: str) -> bool:
19        n=len(word)
20        def helper(j,node):
21            for i in range(j,n):
22                char=word[i]
23                if char==".":  
24                    for child in node.children.values():
25                        if helper(i+1,child):
26                            return True
27                    return False
28                else:
29                    if char not in node.children:
30                        return False
31                    node=node.children[char]
32            return node.is_end
33                    
34        return helper(0,self.root)
35
36        
37        
38
39
40# Your WordDictionary object will be instantiated and called as such:
41# obj = WordDictionary()
42# obj.addWord(word)
43# param_2 = obj.search(word)