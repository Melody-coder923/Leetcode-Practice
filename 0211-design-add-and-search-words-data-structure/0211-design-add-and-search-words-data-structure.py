class TrieNode:
    def __init__(self):
        self.children={}
        self.is_end=False

class WordDictionary:

    def __init__(self):
        self.root=TrieNode()

    def addWord(self, word: str) -> None:
        cur=self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch]=TrieNode()
            cur=cur.children[ch]
        cur.is_end=True

    def search(self, word: str) -> bool:
        def dfs(j, node):
            cur = node
            for i in range(j, len(word)):
                ch = word[i]
                if ch == ".":
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False  # 所有分支都不匹配才返回 False
                else:
                    if ch not in cur.children:
                        return False
                    cur = cur.children[ch]
            return cur.is_end
        return dfs(0, self.root)
            
                    


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)