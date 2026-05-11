1class Solution:
2    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
3        wordDict=set(wordDict)
4        n=len(s)
5        q=deque([0])
6        visited=set()
7        while q:
8            start=q.popleft()
9            if start in visited:
10                continue
11            visited.add(start)
12            for end in range(start+1, n+1):
13                if s[start:end] in wordDict:
14                    if end==n:
15                        return True
16                    q.append(end)
17        return False