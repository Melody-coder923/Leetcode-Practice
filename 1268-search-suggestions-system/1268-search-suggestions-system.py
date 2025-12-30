class Solution:
    class TrieNode:
        def __init__(self):
            self.children = {}
            self.suggestions = []
    class Trie:
        def __init__(self):  
            self.root=Solution.TrieNode()
        
        def insert(self,word):
            cur=self.root
            for c in word:
                if c not in cur.children:
                    cur.children[c]=Solution.TrieNode()
                cur=cur.children[c]
                if len(cur.suggestions) < 3:
                    cur.suggestions.append(word)

        def get_suggestions(self, prefix):
            cur=self.root
            res=[]
            for c in prefix:
                if c in cur.children:
                    cur =cur.children[c]
                    res.append(cur.suggestions)
                else:
                    while len(res) < len(prefix):
                        res.append([])
                    break
            return res
            
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        trie = self.Trie() 
        for product in products:
            trie.insert(product)
        return trie.get_suggestions(searchWord)