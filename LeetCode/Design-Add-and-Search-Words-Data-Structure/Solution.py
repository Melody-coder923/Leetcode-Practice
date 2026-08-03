1class TrieNode:
2    def __init__(self):
3        self.children={}
4        self.end=None
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
19        n=len(word)
20        def dfs(i,node):
21            #base case
22            if i==n:
23                return node.end  
24            char=word[i]
25            if char ==".":
26                for child_char in node.children:
27                    nxt=node.children[child_char]
28                    if dfs(i+1,nxt):
29                        return True
30            else:
31                if char not in node.children:
32                    return False
33                else:
34                    nxt=node.children[char]
35                    if dfs(i+1,nxt):
36                        return True
37            
38            return False
39        
40        return dfs(0,self.root)
41         
42
43
44
45# Your WordDictionary object will be instantiated and called as such:
46# obj = WordDictionary()
47# obj.addWord(word)
48# param_2 = obj.search(word)
49"""
50       root    
51    b        m
52  a   c        a
53d        d.        d
54null
55"""