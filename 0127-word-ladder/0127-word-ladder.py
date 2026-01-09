from collections import deque, defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Edge Case: endWord not in wordList -> return 0
        wordList=set(wordList)
        if endWord not in wordList:
            return 0
        # the shortest transformation sequence - BFS level 统计层
        n=len(beginWord)
        dic=defaultdict(list)
       
        # Step1: beginWord 把每个字母替换为"*" hot-> *ot  h*t ho*
        # 建立dic[list] ---- key-value:   [ *ot] : hot, dot, lot  key和value都是从wordList来的
        for word in wordList:
            for i in range(n): 
                check= word[:i]+"*"+word[i+1:]
                dic[check].append(word)

        # Step2: BFS deque=([(beginWord,level)]) +visited
        q=deque()
        # tuple (word, level)
        q.append((beginWord,1))
        visited=set()
        visited.add(beginWord)
        while q:
            word,level=q.popleft() #hot
            if word==endWord:
                return level
            for i in range(n):
                new_word=word[:i]+"*"+word[i+1:]
                if new_word in dic:
                    for neighbour in dic[new_word]:
                        if neighbour not in visited:
                            visited.add(neighbour)
                            q.append((neighbour,level+1))
                    dic[new_word]=[]
        return 0