from collections import defaultdict, deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList=set(wordList)
        if endWord not in wordList:
            return 0
        
        wordLen=len(beginWord)

        # 映射型字典 : *ot: [hot,dot,lot]
        map = defaultdict(list)
        for word in wordList:
            for i in range(wordLen): 
                key=word[:i]+"*"+word[i+1:]
                map[key].append(word)    
        # BFS 最短路径

        q = deque([(beginWord, 1)])
        visited=set([beginWord])
        while q:
            word,level=q.popleft()
            for i in range(wordLen):
                intermediate= word[:i]+"*"+word[i+1:]

                for neighbour in map[intermediate]:
                    if neighbour==endWord:
                        return level+1
                    if  neighbour not in visited:
                        visited.add(neighbour)
                        q.append((neighbour,level+1))
                map[intermediate]=[]

        return 0

    