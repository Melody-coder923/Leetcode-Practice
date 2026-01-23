class TrieNode():
    def __init__(self):
        self.children={}
        self.is_end=False

class WordDictionary:

    def __init__(self):
        self.root=TrieNode()

    def addWord(self, word: str) -> None:
        cur=self.root
        for c in word:
            if c not in cur.children:
                cur.children[c]=TrieNode()
            cur=cur.children[c]
        cur.is_end=True

    def search(self, word: str) -> bool:
        def helper(j,node):
            cur=node
            for i in range(j,len(word)):
                char=word[i]
                if char==".":
                    for child in cur.children.values():
                        if helper(i+1,child):
                            return True
                    return False
                else:
                    if char not in cur.children:
                        return False
                    cur=cur.children[char]
            return cur.is_end
        return helper(0,self.root)
                

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)