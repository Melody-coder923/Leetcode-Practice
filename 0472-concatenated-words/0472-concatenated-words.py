class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
from functools import lru_cache
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        # 1. 建立 
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.is_word = True
    
        # 2. 检查每个单词是否是连接词
        @lru_cache(maxsize=None)
        def canForm(word, index, count):
            if index==len(word):
                return count>=2
            node=root
            for i in range(index,len(word)):
                char=word[i]
                if char not in node.children:
                    return False
                node = node.children[char]
                if node.is_word:
                    if canForm(word,i+1,count+1):
                        return True
            return False
        
        res=[]
        for word in words:
            if canForm(word,0,0):
                res.append(word)
        return res

