1class Solution:
2    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
3        n=len(s)
4        wordDict=set(wordDict)
5        @lru_cache(None)
6        def dfs(end):
7            #base case
8            if end==0:
9                return [""]
10            # recursive rule
11            res=[]
12            for start in range(end):
13            #break down
14                suffix=s[start:end]
15                if suffix in wordDict:
16                    tmp=dfs(start)
17                    for word in tmp:
18                        res.append((word+" "+ suffix).strip())
19            return res
20        return dfs(n)
21 