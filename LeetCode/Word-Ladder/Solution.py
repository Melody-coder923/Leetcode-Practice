1class Solution:
2    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
3        wordSet = set(wordList)
4        if endWord not in wordSet:
5            return 0
6
7        graph=defaultdict(list)
8        n = len(beginWord)
9        for word in wordList:
10            for i in range(n):
11                p=word[:i]+"*"+word[i+1:]
12                graph[p].append(word)
13
14        q = deque([(beginWord, 1)])
15        visited = set([beginWord])
16        
17        while q:
18            size=len(q)
19            for _ in range(size):
20                word,level=q.popleft()
21                if word==endWord:
22                    return level
23              
24                for i in range(n):
25                    pattern = word[:i] + "*" + word[i + 1:]
26                    for nei in graph[pattern]:
27                        if nei not in visited:
28                            visited.add(nei)
29                            q.append((nei, level + 1))
30        return 0