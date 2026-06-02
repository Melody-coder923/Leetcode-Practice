1class Solution:
2    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
3        wordList=set(wordList)
4        if endWord not in wordList:
5            return 0
6        #build dict
7        pattern=defaultdict(list)
8        for word in wordList:
9            for i in range(len(word)):
10                w=word[:i]+"*"+word[i+1:]
11                pattern[w].append(word)
12        #bfs
13        q = deque([(beginWord,1)])
14        visited=set()
15        visited.add(beginWord)
16        while q:
17            for _ in range(len(q)):
18                word,level=q.popleft()
19                if word==endWord:
20                    return level
21                for i in range(len(word)):
22                    w=word[:i]+"*"+word[i+1:]
23                    for p in pattern[w]:
24                        if p not in visited:
25                            q.append((p,level+1))
26                            visited.add(p)
27        return 0