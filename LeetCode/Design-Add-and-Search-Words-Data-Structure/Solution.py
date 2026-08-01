1class TreeNode:
2    def __init__(self):
3        self.children={}
4        self.end=False
5
6class WordDictionary:
7    def __init__(self):
8        self.root=TreeNode()
9    def addWord(self, word: str) -> None:
10        cur=self.root
11        for c in word:
12            if c not in cur.children:
13                cur.children[c]=TreeNode()
14            cur=cur.children[c]
15        cur.end=True
16
17    def search(self, word: str) -> bool:
18        def dfs(index, node):
19            if index == len(word):
20                return node.end
21            c = word[index]
22            if c != ".":
23                if c not in node.children:
24                    return False
25
26                return dfs(
27                    index + 1,
28                    node.children[c]
29                )
30
31            # "."：尝试所有 children
32            for child in node.children.values():
33                if dfs(index + 1, child):
34                    return True
35
36            return False
37
38        return dfs(0, self.root)
39            
40
41
42# Your WordDictionary object will be instantiated and called as such:
43# obj = WordDictionary()
44# obj.addWord(word)
45# param_2 = obj.search(word)